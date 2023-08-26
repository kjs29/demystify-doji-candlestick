import pandas as pd
import math

def get_correlation_coefficient(row:pd.Series, column_name:str, y:list[float]=None) -> float:
    """
    Calculate the correlation coefficient (r) for a given row of stock closing prices.

    The function takes a row containing a list of closing prices and calculates the correlation 
    coefficient (r) using linear regression model. The coefficient (r) indicates the strength and direction of the 
    linear relationship between the time (in trading days) and the stock's closing price.

    Args:
        row (pandas Series): A row containing a list of the closing prices. The list is extracted using the provided column_name.
        column_name (str): The name of the column containing the list of closing prices.

    Returns:
        float: The correlation coefficient (r), ranging from -1 to 1. A value close to 1 indicates a strong positive
               correlation; a value close to -1 indicates a strong negative correlation; a value close to 0 
               indicates no correlation.

               
    Formulas below: 

        Linear Regression Equation: $y = ax + b$

        Slope (a): $\frac{\Sigma(x-\bar{x})(y-\bar{y})}{\Sigma(x-\bar{x})^{2}}$

        Y-intercept (b): $\bar{y} - b\bar{x}$

        Correlation coefficient (r): $(\frac{\sigma x}{\sigma y})*a(slope)$
    """

    # define x(independent variables) and y(dependent variables)
    if y is None:
        y = row[column_name]
    x = [i for i in range(len(y))]

    # calculate slope for least-squares line
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    slope_numerator = 0
    slope_dinominator = 0

    for i in range(len(x)):
        slope_numerator += ((x[i]-mean_x) * (y[i]-mean_y))
        slope_dinominator += ((x[i]-mean_x) ** 2)
    
    slope = slope_numerator / slope_dinominator

    # calculate standard deviation for x, y
    tmp_x = 0
    tmp_y = 0
    for i in range(len(x)):
        tmp_x += ((x[i] - mean_x) ** 2)
        tmp_y += ((y[i] - mean_y) ** 2)
    
    stdev_x = math.sqrt(tmp_x / (len(x)-1))
    stdev_y = math.sqrt(tmp_y / (len(y)-1))

    if stdev_y == 0:
        return 0
    
    # calculate correlation coefficient
    correlation_coefficient = slope * stdev_x / stdev_y

    return correlation_coefficient
