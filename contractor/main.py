import pandas as pd
import path_initializer
from clean_and_filter import filter_on_expense_date_after, clean_data
from compare import compare, compare_attachments_and_create_result
from join import join_with_daily_expenses_item, join_with_audit_request_and_filter_deleted, \
    join_with_unrejected_daily_expenses, get_audit_request_line_attachments
from contractor.config import PATH, FILTER_DATE
from utils import create_blank_df


def main():
    contractor_cols = ['id', 'expenses_type', 'request_id', 'date_of_expenses',
                       'contractor_name', 'location', 'work_type_id', 'qty']

    print('reading audit_request_lines...')

    df = pd.read_csv(PATH + '\\audit_request_line.csv', usecols=contractor_cols)
    df = df[df['expenses_type'] == 'contractor']
    df = filter_on_expense_date_after(df, FILTER_DATE)

    df = join_with_audit_request_and_filter_deleted(df)
    df = join_with_daily_expenses_item(df)

    num_cols = ['qty', 'work_type_id', 'total_amount']
    df = clean_data(df, num_cols, ['contractor_name', 'location'])

    df = join_with_unrejected_daily_expenses(df)

    unique_ids, df_pairs = compare(df)
    df_audit_request_line_attachments = get_audit_request_line_attachments(unique_ids)

    blank_df = create_blank_df(df.columns)
    compare_attachments_and_create_result(df_audit_request_line_attachments, df_pairs, blank_df)

    print(df)


if __name__ == '__main__':
    main()
