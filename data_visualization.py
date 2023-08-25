import math
import pandas as pd
import matplotlib.pyplot as plt

# Calculate the trend change
def trend_change(row):
    """
    Check if there's a trend change based on the product of the correlation coefficients
    before and after the doji pattern. Helper function for 'create_dataframe'.

    Args:
        row (Series): DataFrame row with correlation coefficients before and after the doji pattern.

    Returns:
        bool: True if there's a trend change, False otherwise.
    """
    return True if row['R_before_Doji'] * row['R_after_Doji'] < 0 else False

def create_dataframe(df, num_days):
    """
    Create a new dataframe containing information about doji patterns and trend changes.

    Args:
        df (DataFrame): Input DataFrame with historical stock data.
        num_days (int): Number of days used to calculate correlation coefficients.

    Returns:
        new_df (DataFrame): New DataFrame with doji dates, correlation coefficients, and trend changes.
    """
    
    # Create a DataFrame with the required columns
    new_df = pd.DataFrame({
        'Doji_Date': pd.to_datetime(df['Date']),
        'R_before_Doji': df[f'correlation_coefficient_past_{num_days}_days'],
        'R_after_Doji': df[f'correlation_coefficient_future_{num_days}_days']
    })

    # Create a new column 'Trend_Change'
    new_df['Trend_Change'] = new_df.apply(lambda row: trend_change(row), axis=1)

    # Remove rows containing NaN values
    new_df = new_df.dropna()

    return new_df

def draw_linear_regression(dates:list[str], y:list[float]):
    """
    This function takes a series of y values representing stock prices and 
    fits a linear regression line to them. 
    It then plots the original data points along with the linear regression line. 
    The color of the line depends on the correlation coefficient's sign, 
    and the function also prints the correlation coefficient on the plot.

    Args:
        dates: A list of stock dates
        y: A list of stock prices
    """
    
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
    intercept = mean_y - slope * mean_x
    
    # calculate standard deviation for x, y
    tmp_x = 0
    tmp_y = 0
    for i in range(len(x)):
        tmp_x += ((x[i] - mean_x) ** 2)
        tmp_y += ((y[i] - mean_y) ** 2)
    
    stdev_x = math.sqrt(tmp_x / (len(x)-1))
    stdev_y = math.sqrt(tmp_y / (len(y)-1))

    # calculate correlation coefficient
    correlation_coefficient = slope * stdev_x / stdev_y
    
    regression_y = [slope * x_i + intercept for x_i in x]
    plt.plot(dates, regression_y, color='green' if correlation_coefficient > 0 else 'red') # draw best fitted line
    plt.scatter(x, y) # Scatterplot with original y-values
    plt.subplots_adjust(left=0.2,bottom=0.2) # give space to sides
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Price Trend')
    plt.legend([f'correlation coefficient = {round(correlation_coefficient, 4)}'])
    # plt.show()

    
