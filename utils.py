import pandas as pd


def create_blank_df(columns):
    blank_row = pd.Series({col: None for col in columns}, dtype=object)
    df_blank = pd.DataFrame(blank_row).transpose()

    return df_blank

