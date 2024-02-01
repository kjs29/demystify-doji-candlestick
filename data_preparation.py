import pandas as pd
from correlation_analysis import get_correlation_coefficient

def collect_closes(row, num_days, future, prefix):
    """
    Function to iterate through the row and collect the past/future closes into a list. 
    
    Helper function for 'add_past_future_close_columns'
    """
    closes = []
    for i in range(1, num_days+1) if future else range(num_days, 0, -1):
        closes.append(row[f'{prefix}({i})'])
    return closes

def collect_dates(row, num_days, future, prefix):
    """
    Function to iterate through the row and collect the past/future dates into a list. 

    Helper function for 'add_past_future_date_columns'
    """
    dates = []
    for i in range(1, num_days+1) if future else range(num_days, 0, -1):
        dates.append(row[f'{prefix}({i})'])
    return dates

def add_past_future_close_columns(df: pd.DataFrame, num_days: int, future: bool) -> None:
    """
    Adds columns to the DataFrame that contain either past or future days' closing prices.

    This function extends the DataFrame by adding columns representing the closing prices for the specified number of past or future days. 
    If 'future' is set to True, the function adds columns representing the future closing prices, 
    otherwise, it adds columns for the past closing prices.

    Args:
        df (pd.DataFrame): The DataFrame containing the stock data, including a 'Close' column with closing prices.
        num_days (int): The number of past or future days for which the closing prices are to be added.
        future (bool): If True, adds columns for future closing prices. If False, adds columns for past closing prices.

    Returns:
        None: The function modifies the DataFrame in-place and does not return a value.

    Example:
        If num_days is 5 and future is False, the function will add five columns to the DataFrame
        containing the closing prices for the past five days.
    """

    prefix = "nth_day_future_close" if future else "nth_day_past_close"
    shift_direction = -1 if future else 1
    column_name = f"future_{str(num_days)}_days" if future else f"past_{str(num_days)}_days"

    # Iterate through the range and create new columns based on the shift direction
    for i in range(1, num_days + 1):
        col_name = f'{prefix}({i})'
        df[col_name] = df['Close'].shift(shift_direction * i).round(4)
    
    # Apply the function 'collect_closes' to collect the past/future closes
    df[column_name] = df.apply(lambda row: collect_closes(row, num_days, future, prefix), axis=1)
    
    # Delete the temporary columns
    for i in range(1, num_days + 1):
        df.drop(f'{prefix}({i})', axis=1, inplace=True)

def add_past_future_date_columns(df: pd.DataFrame, num_days: int, future: bool) -> None:
    """
    Adds columns to the DataFrame that contain either past or future dates.
    """
    df['Date'] = pd.to_datetime(df['Date'])

    prefix = "nth_day_future_date" if future else "nth_day_past_date"
    shift_direction = -1 if future else 1
    column_name = f"future_{str(num_days)}_dates" if future else f"past_{str(num_days)}_dates"
    
    for i in range(1, num_days + 1):
        col_name = f'{prefix}({i})'
        df[col_name] = df['Date'].shift(shift_direction * i).dt.strftime('%Y-%m-%d')
    
    # Apply the function 'collect_dates' to collect the past/future dates
    df[column_name] = df.apply(lambda row: collect_dates(row, num_days, future, prefix), axis=1)

    # Delete the temporary columns
    for i in range(1, num_days + 1):
        df.drop(f'{prefix}({i})', axis=1, inplace=True)

def remove_non_numeric_symbols(df:pd.DataFrame, cols:list[str]):
    """
    Iterates through cols and remove all the non-numeric symbols and dot(.) and cast to float type.
    
    For example,
    if cols = ['Close','Open','High','Low'], it removes all non-numeric symbols under each columns 'Close','Open','High','Low'.
    """
    for col in cols:
        # if col data is object(str)
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(r'[^\d.]', '')
            df[col] = df[col].astype(float)

def is_doji(row, error_margin_percentage):
    """
    Checks whether a particular row represents a doji candlestick pattern in stock data.

    Helper function for 'add_doji_column'.
    """
    
    error_range = row['Close'] * error_margin_percentage / 100
    return abs(row['Close'] - row['Open']) <= error_range

def add_doji_column(df: pd.DataFrame, error_margin_percentage=0.05) -> None:
    """
    Adds a 'doji' column to the DataFrame indicating whether the opening price is equal to the closing price.

    Args:
        df (pd.DataFrame): The DataFrame containing the stock data, including 'Open' and 'Close' columns.

    Returns:
        None: The function modifies the DataFrame in-place and does not return a value.
    """
    df['Close'] = pd.to_numeric(df['Close'])
    df['Margin_of_error'] = df['Close'] * error_margin_percentage / 100
    df['doji'] = df.apply(lambda row: is_doji(row, error_margin_percentage), axis=1)

def add_correlation_coefficient_column(df: pd.DataFrame, num_days: int, future: bool) -> None:
    """
    Add the correlation coefficient column to the DataFrame for the given number of past or future days.

    This function also calls the 'add_past_future_date_columns' to add necessary columns for plotting necessary dates to visualize dates in X axis.
    
    For example,
    if num_days == 5, future == True, it will add a column 'correlation_coefficient_future_5_days' to df.

    This function first calls the 'add_past_future_close_columns' function to add necessary columns, 
    then computes the correlation coefficients using the 'get_correlation_coefficient' function and adds the results to the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the stock data.
        num_days (int): Number of days to consider in the calculation.
        future (bool): Whether to consider future days (True) or past days (False).

    Returns:
        None: The function modifies the DataFrame in-place and does not return a value.
    """

    # Call 'add_past_future_close_columns' function to prepare calculations
    add_past_future_close_columns(df, num_days, future)

    # Call 'add_past_future_date_columns' function to prepare displaying dates on x-axis
    add_past_future_date_columns(df, num_days, future)

    # Construct the correct column name based on num_days and future setting
    column_name = f'future_{str(num_days)}_days' if future else f'past_{str(num_days)}_days'

    # Apply 'get_correlation_coefficient' to each row, passing the correct column name
    df[f'correlation_coefficient_future_{str(num_days)}_days' if future else f'correlation_coefficient_past_{str(num_days)}_days'] = \
        df.apply(lambda row: get_correlation_coefficient(row, column_name), axis=1)
