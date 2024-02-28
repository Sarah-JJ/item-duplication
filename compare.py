import pandas as pd
import re


def get_duplication_probability(row1, row2):
    duplication_probability = 0

    project_col = 'project'
    project1 = row1[project_col]
    project2 = row2[project_col]

    if project1 == project2:
        duplication_probability += 0.2

    expense_date_col = 'date_of_expenses'
    not_empty = not pd.isna(row1[expense_date_col]) and not pd.isna(row2[expense_date_col])
    if not_empty and row1[expense_date_col] == row2[expense_date_col]:
        duplication_probability += 0.25

    contractor_col = 'contractor_name'
    contractor1 = row1[contractor_col]
    contractor2 = row2[contractor_col]

    project_col = 'project'
    row1_total = row1[project_col]
    row2_total = row2[project_col]

    if row1_total > 0 and row2_total > 0:
        if row1_total == row2_total:
            duplication_probability += 30
        else:
            ratio1_2 = row1_total / row2_total
            ratio2_1 = row2_total / row1_total
            if 0.8 <= ratio1_2 < 1 or 0.8 <= ratio2_1 < 1:
                duplication_probability += 10

    attachment_field = 'Main Attachment/Name'
    row1_attachment_name = str.lower(str(row1[attachment_field]))
    row2_attachment_name = str.lower(str(row2[attachment_field]))

    if row1_attachment_name != "" and row2_attachment_name != "":
        if row1_attachment_name == row2_attachment_name:
            duplication_probability += 40
        else:
            row1_normalized_name = re.sub(r'(\(\d+\)\s*)+(?=\.\w+)', '', row1_attachment_name)
            row2_normalized_name = re.sub(r'(\(\d+\)\s*)+(?=\.\w+)', '', row2_attachment_name)

            if row1_normalized_name == row2_normalized_name:
                duplication_probability += 15

    if not pd.isna(row1['Timesheet Line/Date']) and not pd.isna(row2['Timesheet Line/Date']):
        if row1['Timesheet Line/Date'] == row2['Timesheet Line/Date']:
            if str.lower(row1['Task Type']) == 'cb' and str.lower(row2['Task Type']) == 'cb':
                duplication_probability += 5
            else:
                duplication_probability += 25

    sum_value_1 = sum(row1[column] for column in meter_cols)
    sum_value_2 = sum(row2[column] for column in meter_cols)

    if sum_value_1 > 0 and sum_value_2 > 0:
        if sum_value_1 == sum_value_2:
            duplication_probability += 50
        else:
            sum_ratio1_2 = sum_value_1 / sum_value_2
            sum_ratio2_1 = sum_value_2 / sum_value_1
            if 0.8 <= sum_ratio1_2 < 1 or 0.8 <= sum_ratio2_1 < 1:
                duplication_probability += 10

    return duplication_probability


def compare(df, df_blank):
    high, low, mod = [], [], []

    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            print(f"Comparing record {row1['Name']},{row2['Name']}...")
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
