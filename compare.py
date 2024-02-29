import pandas as pd
from Levenshtein import ratio
from columns_check_config import check_cols_for_equality, text_cols
from consts import COMPARE_WITH_LEVENSHTEIN, MIN_PROBABILITY, print_separator


def calculate_text_similarity_ratio(row1, row2, col, total_contribution_to_duplication):
    value1 = row1[col]
    value2 = row2[col]

    if COMPARE_WITH_LEVENSHTEIN:
        similarity_percent = ratio(value1, value2)
        if similarity_percent >= 0.75:
            return similarity_percent * total_contribution_to_duplication
        else:
            return 0

    elif value1 == value2:
        return total_contribution_to_duplication

    else:
        return 0


def calculate_equality_ratio(row1, row2, col, total_contribution_to_duplication):
    value1 = row1[col]
    value2 = row2[col]

    if value1 == value2:
        return total_contribution_to_duplication
    return 0


def get_duplication_probability(row1, row2):
    duplication_probability = 0

    for col in check_cols_for_equality:
        duplication_probability += calculate_equality_ratio(row1, row2, col['name'], col['contribution'])

    for col in text_cols:
        duplication_probability += calculate_text_similarity_ratio(row1, row2, col['name'], col['contribution'])

    # TODO: compare attachments

    return duplication_probability


def compare(df, df_blank):
    high, low, mod = [], [], []

    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            # print(f"Comparing record {index1},{index2}...")
            if index1 >= index2:
                continue

            probability = get_duplication_probability(row1, row2)

            if probability < MIN_PROBABILITY:
                continue

            row1['similarity'] = probability
            row2['similarity'] = probability

            df_row1 = pd.DataFrame(row1).transpose()
            df_row2 = pd.DataFrame(row2).transpose()

            if probability > 0.7:
                high.extend([df_row1, df_row2, df_blank])
            elif probability > 0.4:
                mod.extend([df_row1, df_row2, df_blank])
            elif probability > 0.1:
                low.extend([df_row1, df_row2, df_blank])

    return high, mod, low
