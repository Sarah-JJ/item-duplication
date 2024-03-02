import pandas as pd
from Levenshtein import ratio

from column_weights import CHECK_FOR_EQUALITY_COLS, TEXT_COLS, ATTACHMENTS_WEIGHT
from consts import COMPARE_WITH_LEVENSHTEIN, MIN_SIMILARITY, SIMILARITY_LEVELS, print_separator
from create_result import create_result


def calculate_text_similarity_ratio(row1, row2, col, col_weight):
    value1 = row1[col]
    value2 = row2[col]

    if COMPARE_WITH_LEVENSHTEIN:
        similarity_percent = ratio(value1, value2)
        if similarity_percent >= 0.75:
            return similarity_percent * col_weight
        else:
            return 0

    elif value1 == value2:
        return col_weight

    else:
        return 0


def calculate_equality_ratio(row1, row2, col, total_contribution_to_duplication):
    value1 = row1[col]
    value2 = row2[col]

    if value1 == value2:
        return total_contribution_to_duplication
    return 0


def calculate_pair_similarity_percent(row1, row2):
    duplication_percent = 0

    for col in CHECK_FOR_EQUALITY_COLS:
        duplication_percent += calculate_equality_ratio(row1, row2, col['name'], col['contribution'])

    for col in TEXT_COLS:
        duplication_percent += calculate_text_similarity_ratio(row1, row2, col['name'], col['contribution'])

    return duplication_percent


def compare(df):
    unique_ids = set()
    df_pairs = []

    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            print(f"Comparing record {index1},{index2}...")
            if index1 >= index2:
                continue

            similarity_percent = calculate_pair_similarity_percent(row1, row2)

            if (similarity_percent + 0.1) < MIN_SIMILARITY:
                continue

            unique_ids.add(row1['id'])
            unique_ids.add(row2['id'])

            df_row1 = pd.DataFrame(row1).transpose()
            df_row2 = pd.DataFrame(row2).transpose()

            df_pair_dict = {
                'item1': {
                    'id': df_row1['id'].tolist()[0],
                    'item': df_row1
                },
                'item2': {
                    'id': df_row2['id'].tolist()[0],
                    'item': df_row2
                },
                'similarity': similarity_percent
            }

            df_pairs.append(df_pair_dict)

    return unique_ids, df_pairs


def calculate_attachments_similarity(attachments_set1, attachments_set2):
    intersecting_elements = attachments_set1 & attachments_set2
    intersection_count = len(intersecting_elements)

    attachments1_intersection_ratio = intersection_count / len(attachments_set1)
    attachments2_intersection_ratio = intersection_count / len(attachments_set2)

    intersection_ratio = (attachments1_intersection_ratio + attachments2_intersection_ratio) / 2
    return intersection_ratio * ATTACHMENTS_WEIGHT


def compare_attachments_and_create_result(df_audit_request_line_attachments, df_pairs, df_blank):
    high, mod, low = [], [], []

    for df_pair in df_pairs:
        item1 = df_pair['item1']
        df1 = item1['item']
        id1 = item1['id']

        item2 = df_pair['item2']
        df2 = item2['item']
        id2 = item2['id']

        print(f'{df1}, {print_separator}')
        print(f'{df2}, {print_separator + print_separator}')

        print(f'{id1}, {print_separator}')
        print(f'{id2}, {print_separator}')

        df1_attachments = df_audit_request_line_attachments[
            df_audit_request_line_attachments['audit_request_line_id'] == id1]
        attachments_set1 = set(df1_attachments['name'])

        df2_attachments = df_audit_request_line_attachments[
            df_audit_request_line_attachments['audit_request_line_id'] == id2]
        attachments_set2 = set(df2_attachments['name'])

        updated_similarity = (df_pair['similarity'] +
                              calculate_attachments_similarity(attachments_set1, attachments_set2))

        row1_attachments = ', '.join(attachments_set1)
        df1['attachments'] = row1_attachments
        df1['similarity'] = updated_similarity

        row2_attachments = ', '.join(attachments_set2)
        df2['attachments'] = row2_attachments
        df2['similarity'] = updated_similarity

        if updated_similarity > SIMILARITY_LEVELS['high']:
            high.extend([df1, df2, df_blank])
        elif updated_similarity > SIMILARITY_LEVELS['mod']:
            mod.extend([df1, df2, df_blank])
        elif updated_similarity > SIMILARITY_LEVELS['low']:
            low.extend([df1, df2, df_blank])

    create_result(high, 'high.csv')
    create_result(mod, 'mod.csv')
    create_result(low, 'low.csv')
