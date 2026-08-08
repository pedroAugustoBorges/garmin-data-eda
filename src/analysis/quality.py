import pandas as pd


def load_structure_df(df:pd.DataFrame):
    rows = len(df)
    columns_count = len(df.columns)
    columns = df.columns
    
    print(rows)
    print(columns_count)
    print(columns)