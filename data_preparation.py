import pandas as pd

# Function to iterate through the row and collect the past/future closes into a list
def collect_closes(row, num_days, future, prefix):
    """
    Helper function for 'add_past_future_close_columns'
    """
    closes = []
    for i in range(1, num_days+1) if future else range(num_days, 0, -1):
        closes.append(row[f'{prefix}({i})'])
    return closes

def collect_dates(row, num_days, future, prefix):
    """
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
    df['Margin_of_error'] = df['Close'] * error_margin_percentage / 100
    df['doji'] = df.apply(lambda row: is_doji(row, error_margin_percentage), axis=1)
