import pandas as pd

def correlation_matrix(df: pd.DataFrame, method : str = "person"):
    return df.corr(method, numeric_only= True)


def correlation_target (df: pd.DataFrame, target : str, method : str = "pearson"):
    return df.corr(method, numeric_only= True)[target]


