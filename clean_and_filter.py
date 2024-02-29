import pandas as pd
from consts import normalize_arabic_text_in_columns
from normalize_arabic_text import normalize_arabic_text as normalize


def filter_on_expense_date_after(df, date_value):
    df['date_of_expenses'] = pd.to_datetime(df['date_of_expenses'])

    filter_date = pd.to_datetime(date_value)
    filtered_df = df[df['date_of_expenses'] > filter_date]

    return filtered_df


def clean_data(df, num_cols=[], text_cols=[], date_cols=[]):
    print('cleaning data...')
    type_cast_and_fillna(df, num_cols, date_cols)

    df[text_cols] = df[text_cols].astype(str)
    df[text_cols] = df[text_cols].apply(lambda x: x.str.strip())
    df[normalize_arabic_text_in_columns] = df[normalize_arabic_text_in_columns].applymap(lambda x: normalize(x))

    return df


def type_cast_and_fillna(df, num_columns, date_cols):
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    for col in num_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    return df
