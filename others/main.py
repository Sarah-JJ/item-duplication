import pandas as pd
import path_initializer
from clean_and_filter import filter_on_expense_date_after, clean_data, normalize_arabic_text
from compare import compare, compare_attachments_and_create_result, create_result
from join import join_with_daily_expenses_item, join_with_audit_request_and_filter_deleted, \
    join_with_unrejected_daily_expenses, get_audit_request_line_attachments
from others.column_weights import TEXT_COMPARISON_COLS, EQUALITY_COMPARISON_COLS, ATTACHMENTS_WEIGHT
from others.config import PATH, FILTER_DATE, NORMALIZE_ARABIC_COLS, SIMILARITY_THRESHOLD, COMPARE_WITH_LEVENSHTEIN, \
    SIMILARITY_LEVELS, COMPARE_WITH_RECORDS_CREATED_DAYS_BEFORE, COMPARE_WITH_RECORDS_CREATED_DAYS_AFTER
from utils import create_blank_df


def main():
    columns = ['id', 'description_of_case', 'others_name', 'amount',
               'date_of_expenses', 'expenses_type', 'request_id', 'create_date']

    print('reading audit_request_lines...')

    df = pd.read_csv(PATH + '\\audit_request_line.csv', usecols=columns)
    df = df[df['expenses_type'] == 'others']
    df = filter_on_expense_date_after(df, FILTER_DATE)

    df = join_with_audit_request_and_filter_deleted(df, PATH)
    df = join_with_daily_expenses_item(df, PATH)

    df = clean_data(df, [], [col['name'] for col in TEXT_COMPARISON_COLS], ['create_date'])
    df = normalize_arabic_text(df, NORMALIZE_ARABIC_COLS)

    df = join_with_unrejected_daily_expenses(df, PATH, ['id', 'state', 'project_id'])

    unique_ids, df_pairs = compare(df, EQUALITY_COMPARISON_COLS, TEXT_COMPARISON_COLS,
            ATTACHMENTS_WEIGHT, SIMILARITY_THRESHOLD, COMPARE_WITH_LEVENSHTEIN, COMPARE_WITH_RECORDS_CREATED_DAYS_AFTER,
            COMPARE_WITH_RECORDS_CREATED_DAYS_BEFORE)
    df_audit_request_line_attachments = get_audit_request_line_attachments(unique_ids, PATH)

    # creating blank_df outside the method to avoid overhead of creating a blank df multiple times with every iteration
    blank_df = create_blank_df(df.columns)
    compare_attachments_and_create_result(df_audit_request_line_attachments, df_pairs, blank_df,
                                          ATTACHMENTS_WEIGHT, SIMILARITY_LEVELS)


if __name__ == '__main__':
    main()
