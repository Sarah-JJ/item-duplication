import pandas as pd


def create_result_df(df_list, output_file):
    print('creating dataframes...')

    df = pd.DataFrame(columns=df_list[0].columns)
    df['similarity'] = df['similarity'].astype('float64')
    df = pd.concat(df_list)
    df.reset_index(drop=True, inplace=True)

    print(f'creating {output_file} ...')
    df.to_excel(output_file, index=False)
