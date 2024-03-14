import pandas as pd


def create_output_files(df_list, output_file=''):
    print('creating dataframes...')

    if df_list:
        df = pd.DataFrame(columns=df_list[0].columns)
        df['similarity'] = df['similarity'].astype('float64')

        df = pd.concat(df_list)
        df.reset_index(drop=True, inplace=True)

        print(f'creating {output_file} ...')
        df.to_csv(output_file, index=False)
