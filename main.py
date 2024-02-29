import pandas as pd
from clean_and_filter import filter_on_expense_date_after, clean_data
from compare import compare
from create_result import create_result_df
from join import join_with_daily_expenses_item, join_with_audit_request_and_filter_deleted, \
    join_with_unrejected_daily_expenses
from consts import path, filter_date


def main():
    contractor_cols = ['id', 'expenses_type', 'request_id', 'date_of_expenses',
                       'contractor_name', 'location', 'work_type_id', 'qty']

    print('reading audit_request_lines...')

    df = pd.read_csv(path + '\\audit_request_line.csv', usecols=contractor_cols)
    df = df[df['expenses_type'] == 'contractor']
    df = filter_on_expense_date_after(df, filter_date)

    df = join_with_audit_request_and_filter_deleted(df)
    df = join_with_daily_expenses_item(df)

    num_cols = ['qty', 'work_type_id', 'total_amount']
    df = clean_data(df, num_cols, ['contractor_name', 'location'])

    df = join_with_unrejected_daily_expenses(df)

    blank_row = pd.Series({col: None for col in df.columns}, dtype=object)
    df_blank = pd.DataFrame(blank_row).transpose()

    high, mod, low = compare(df, df_blank)

    create_result_df(high, 'high.xlsx')
    create_result_df(mod, 'mod.xlsx')
    create_result_df(low, 'low.xlsx')

    print(df)


if __name__ == '__main__':
    main()
