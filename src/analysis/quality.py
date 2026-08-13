import pandas as pd


def load_structure_df(df:pd.DataFrame):
    rows = len(df)
    columns_count = len(df.columns)
    columns = df.columns
    df_infos = df.dtypes
    
    return f"""Linhas: {rows}, 
            \nQuantidade de Colunas: {columns_count}\n
            Colunas: {columns} \n
            Estrutura das colunas: {df_infos}"""