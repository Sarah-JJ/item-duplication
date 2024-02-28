import pandas as pd
from clean_and_filter import filter_on_expense_date_after, clean_data
from join import join_with_daily_expenses_item, join_with_audit_request_and_filter_deleted, \
    join_with_unrejected_daily_expenses
from consts import path, filter_date


def main():
    contractor_cols = ['id', 'expenses_type', 'request_id', 'date_of_expenses',
                       'contractor_name', 'location', 'work_type_id', 'qty', 'price_per_unit']

    print('reading audit_request_lines...')
    df = pd.read_csv(path + '\\audit_request_line.csv', usecols=contractor_cols)
    df = filter_on_expense_date_after(df, filter_date)

    print('cleaning data...')
    num_cols = ['qty', 'price_per_unit']
    df = clean_data(df, num_cols, ['contractor_name', 'location'])

    df = join_with_audit_request_and_filter_deleted(df)
    df = join_with_daily_expenses_item(df)
    df = join_with_unrejected_daily_expenses(df)

    print(df)


if __name__ == '__main__':
    main()
