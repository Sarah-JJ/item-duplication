import pandas as pd
from Levenshtein import ratio
from create_result import create_result


def calculate_text_similarity_ratio(value1, value2, col_weight, compare_with_levenshtein, levenshtein_threshold):
    if compare_with_levenshtein:
        similarity_percent = ratio(value1, value2)
        if similarity_percent >= levenshtein_threshold:
            return similarity_percent * col_weight
        else:
            return 0

    elif value1 == value2:
        return col_weight
    else:
        return 0


def calculate_equal_columns_ratio(row1, row2, col, weight):
    value1 = row1[col]
    value2 = row2[col]

    if value1 == value2:
        return weight
    return 0


def compare(df, equality_comparison_cols, text_comparison_cols, attachments_weight, similarity_threshold, compare_with_levenshtein):
    unique_ids = set()
    df_pairs = []

    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            print(f"Comparing record {index1},{index2}...")
            if index1 >= index2:
                continue

            similarity_percent = 0

            for col in equality_comparison_cols:
                similarity_percent += calculate_equal_columns_ratio(row1, row2, col['name'], col['weight'])

            for col in text_comparison_cols:
                similarity_percent += calculate_text_similarity_ratio(row1[col['name']], row2[col['name']], col['weight'], compare_with_levenshtein, col['levenshtein_threshold'])

            if (similarity_percent + attachments_weight) < similarity_threshold:
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


def calculate_attachments_similarity(attachments_set1, attachments_set2, weight):
    intersecting_elements = attachments_set1 & attachments_set2
    intersection_count = len(intersecting_elements)

    attachments1_intersection_ratio = intersection_count / len(attachments_set1)
    attachments2_intersection_ratio = intersection_count / len(attachments_set2)

    intersection_ratio = (attachments1_intersection_ratio + attachments2_intersection_ratio) / 2
    return intersection_ratio * weight


def compare_attachments_and_create_result(df_audit_request_line_attachments, df_pairs, df_blank, weight, similarity_levels):
    high, mod, low = [], [], []

    for df_pair in df_pairs:
        item1 = df_pair['item1']
        df1 = item1['item']
        id1 = item1['id']

        item2 = df_pair['item2']
        df2 = item2['item']
        id2 = item2['id']

        df1_attachments = df_audit_request_line_attachments[
            df_audit_request_line_attachments['audit_request_line_id'] == id1]
        attachments_set1 = set(df1_attachments['name'])

        df2_attachments = df_audit_request_line_attachments[
            df_audit_request_line_attachments['audit_request_line_id'] == id2]
        attachments_set2 = set(df2_attachments['name'])

        updated_similarity = (df_pair['similarity'] +
                              calculate_attachments_similarity(attachments_set1, attachments_set2, weight))

        row1_attachments = ', '.join(attachments_set1)
        df1['attachments'] = row1_attachments
        df1['similarity'] = updated_similarity

        row2_attachments = ', '.join(attachments_set2)
        df2['attachments'] = row2_attachments
        df2['similarity'] = updated_similarity

        if updated_similarity > similarity_levels['high']:
            high.extend([df1, df2, df_blank])
        elif updated_similarity > similarity_levels['mod']:
            mod.extend([df1, df2, df_blank])
        elif updated_similarity > similarity_levels['low']:
            low.extend([df1, df2, df_blank])

    create_result(high, 'high.csv')
    create_result(mod, 'mod.csv')
    create_result(low, 'low.csv')
