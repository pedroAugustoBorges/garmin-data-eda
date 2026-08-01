import pandas as pd

def groupy_by_column(df:pd.DataFrame, column):
    return df.groupby(column)


def groupy_by_column_month(df:pd.DataFrame, column):
    return df.groupby(pd.Grouper(key=column, freq="ME"))



def agg_by_mes(df:pd.DataFrame, date_column:str, **agg_kwargs):
    return (groupy_by_column_month(df, date_column)
            .agg(**agg_kwargs))