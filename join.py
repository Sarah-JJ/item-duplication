import pandas as pd
from consts import print_separator, PATH


def join_with_audit_request_and_filter_deleted(df):
    print('reading audit_requests...')

    cols = ['id', 'item_id']
    df_audit_request = pd.read_csv(PATH + '\\audit_request.csv', usecols=cols)
    df_result = pd.merge(df, df_audit_request, left_on='request_id',
                         right_on='id', suffixes=('', '_audit_request'))
    df_result.drop('id_audit_request', axis=1, inplace=True)

    df_result = df_result[df_result['item_id'].notna() & (df_result['item_id'] != '')]

    print(f'{df_result}{print_separator}')

    return df_result


def join_with_daily_expenses_item(df):
    print('reading daily expense items...')

    cols = ['id', 'daily_expenses_id', 'total_amount']
    df_daily_expenses_item = pd.read_csv(PATH + '\\daily_expenses_item.csv', usecols=cols)
    df_result = pd.merge(df, df_daily_expenses_item, left_on='item_id',
                         right_on='id', suffixes=('', '_daily_expenses_item'))
    df_result.drop('id_daily_expenses_item', axis=1, inplace=True)
    print(f'{df_result}{print_separator}')

    return df_result


def join_with_unrejected_daily_expenses(df):
    print('reading daily expenses...')

    cols = ['id', 'project_id', 'state']
    df_daily_expenses = pd.read_csv(PATH + '\\daily_expenses.csv', usecols=cols)
    df_daily_expenses = df_daily_expenses[df_daily_expenses['state'] != 'rejected']
    print(f'{df_daily_expenses} {print_separator}')

    df_result = pd.merge(df, df_daily_expenses, left_on='daily_expenses_id',
                         right_on='id', suffixes=('', '_daily_expenses'))
    df_result.drop('id_daily_expenses', axis=1, inplace=True)
    print(f'{df_result}{print_separator}')

    return df_result
