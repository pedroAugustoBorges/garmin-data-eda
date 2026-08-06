import pandas as pd
import numpy as np

def correlation_matrix(df: pd.DataFrame, method : str = "person"):
    return df.corr(method, numeric_only= True)


def correlation_target (df: pd.DataFrame, target : str, method : str = "pearson"):
    return df.corr(method, numeric_only= True)[target]


def correlation_pearson(x, y):
    
    
    x = np.array(x)
    y = np.array(y)
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    
    print("x, y")
    print(x, y)
    
    print("mean")
    print(x_mean, y_mean)
    
    
    print("centered")
    x_centered  = x - x_mean
    y_centered = y - y_mean
    
    print(x_centered, y_centered)
    
    print("covariannce_sum")
    
    covariance_sum = np.sum(x_centered * y_centered)
    print(covariance_sum)

    
    print("squared_deviation")
    
    x_squared_deviation = np.sum(x_centered ** 2)
    y_squared_deviation = np.sum(y_centered ** 2)
    print(x_squared_deviation, y_squared_deviation)

    
    
    x_y_matriz = x_squared_deviation * y_squared_deviation
    std_product = np.sqrt(x_y_matriz)
    print(x_y_matriz)
    
    r = covariance_sum / std_product
    
    print(r)
    
    

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

correlation_pearson(x, y)