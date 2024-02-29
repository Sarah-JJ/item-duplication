import pandas as pd
from Levenshtein import ratio
from consts import compare_using_levenshtein_distance, print_separator


def compare_text_col_ratio(row1, row2, col, total_contribution_to_duplication):
    value1 = row1[col]
    value2 = row2[col]

    if compare_using_levenshtein_distance:
        similarity_percent = ratio(value1, value2)
        if similarity_percent > 0.75:
            print(value1)
            print(value2)
            print(similarity_percent)
            print(print_separator)
            print('\n')
            return similarity_percent * total_contribution_to_duplication
        else:
            return 0

    elif value1 == value2:
        return total_contribution_to_duplication

    else:
        return 0


def get_duplication_probability(row1, row2):
    duplication_probability = 0

    project_col = 'project_id'
    project1 = row1[project_col]
    project2 = row2[project_col]

    if project1 == project2:
        duplication_probability += 0.2

    expense_date_col = 'date_of_expenses'
    not_empty = not pd.isna(row1[expense_date_col]) and not pd.isna(row2[expense_date_col])
    if not_empty and row1[expense_date_col] == row2[expense_date_col]:
        duplication_probability += 0.25

    duplication_probability += compare_text_col_ratio(row1, row2, 'contractor_name', 0.1)
    duplication_probability += compare_text_col_ratio(row1, row2, 'location', 0.1)

    work_type_col = 'work_type_id'
    work_type1 = row1[work_type_col]
    work_type2 = row2[work_type_col]

    if work_type1 == work_type2:
        duplication_probability += 0.1

    quantity_col = 'qty'
    qty1 = row1[quantity_col]
    qty2 = row2[quantity_col]

    if qty1 == qty2:
        duplication_probability += 0.1

    # TODO: compare attachments

    return duplication_probability


def compare(df, df_blank):
    high, low, mod = [], [], []

    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            print(f"Comparing record {index1},{index2}...")
            if index1 >= index2:
                continue

            probability = get_duplication_probability(row1, row2)
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
