import pandas as pd


def filter_on_expense_date_after(df, date_value):
    df['date_of_expenses'] = pd.to_datetime(df['date_of_expenses'])

    filter_date = pd.to_datetime(date_value)
    filtered_df = df[df['date_of_expenses'] > filter_date]

    return filtered_df


def clean_data(df, num_columns):
    for col in num_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    return df