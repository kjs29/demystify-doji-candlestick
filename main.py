import random
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi

from data_preparation import (
    add_doji_column,
    add_correlation_coefficient_column,
    remove_non_numeric_symbols
)
from data_visualization import (
    create_dataframe, 
    draw_linear_regression
)

def main(filename, training_days=20, test_different_time=False, count=0):
    # Import dataset
    df = pd.read_csv(filename)

    # Rename a column name
    df.rename(columns={'Close/Last': 'Close'}, inplace=True)

    # If test_different_time is True, randomly select a subset of rows from the DataFrame
    if test_different_time:
        starting_index = random.randint(0,len(df)-2)
        ending_index = random.randint(starting_index+1, len(df)-1)
        df = df.iloc[starting_index: ending_index]
    training_date_begin = df.iloc[len(df)-1]['Date']
    training_date_end = df.iloc[0]['Date']

    # Remove non-numeric symbols in the columns and convert to float type
    cols = ['Close','Open','High','Low']
    remove_non_numeric_symbols(df, cols)

    # Convert the 'Date' column to datetime format for easier manipulation
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort the DataFrame by the 'Date' column in ascending order
    df = df.sort_values(by='Date', ascending=True)

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Add correlation coefficient columns for specified training days (both past and future)
    add_correlation_coefficient_column(df, training_days, future=False)
    add_correlation_coefficient_column(df, training_days, future=True)

    # Add a 'doji' column to the DataFrame
    add_doji_column(df, error_margin_percentage=0)

    # Filter out rows where 'doji' is True and save this subset as a new CSV
    doji_df = df[df['doji']==True]
    doji_df.to_csv('doji.csv')

    # For each doji, save images; scatterplots and linear regression lines for past and future training days
    for i in doji_df.index:
        past_dates = df.iloc[i][f'past_{training_days}_dates']
        draw_linear_regression(past_dates, df.iloc[i][f'past_{training_days}_days'])
        plt.savefig(f'pictures/past_{training_days}_days_{i}.png')
        plt.close()

        future_dates = df.iloc[i][f'future_{training_days}_dates']
        draw_linear_regression(future_dates, df.iloc[i][f'future_{training_days}_days'])
        plt.savefig(f'pictures/future_{training_days}_days_{i}.png')
        plt.close()

    # Create a summary DataFrame based on the doji DataFrame
    snapshot_df = create_dataframe(doji_df, training_days)

    # Save the snapshot DataFrame as an image
    dfi.export(snapshot_df, f'result_{count}.png')

    # Filter rows where trend changes after a doji
    trend_change_row = snapshot_df[snapshot_df['Trend_Change']==True]

    # Display the test period and the snapshot DataFrame
    print(f'Test period({count}): {training_date_begin} ~ {training_date_end}')
    print(snapshot_df)
    
    # Calculate and display the probability of a trend change after a doji appearance
    try:
        probability_of_doji_reversal = round(len(trend_change_row) / len(snapshot_df)*100,4)
        print(f'Probability of trend change after a doji appearance: {probability_of_doji_reversal}%')
        snapshot_df.to_csv('Result_' + filename)
        return probability_of_doji_reversal
    except ZeroDivisionError:
        print(f'There is no doji appearance.\n')

    return None


# Initialize counters and parameters
total = 0
count = 0

# Parameters - Modify to test different inputs
num_samples = 1
filename = 'HistoricalData_SPY_from_Nasdaq.csv'
training_days = 10
test_different_time = False

# if test_different_time is True
if test_different_time == True:
    # If no doji is found, exit the program
    if main(filename, training_days, False) is None:
        print("No doji found in the entire dataset. Exiting the program.")
    # Run the main function multiple times, accumulating results when a doji appears
    else:
        while count < num_samples:
            result = main(filename, training_days, test_different_time, count=count)
            if result is not None:
                total += result
                count += 1
            print(f'count/total_num_samples:{count}/{num_samples}, total:{total}\n------')
        # Display the final accumulated results
        print(f'Total added probability: {total}% / Count: {count}')
        print(f'Mean probability: {total/num_samples:.2f}%')
# if test_different_time is False
else:
    while count < num_samples:
        result = main(filename, training_days, test_different_time, count=count)
        if result is not None:
            total += result
            count += 1
        print(f'count/total_num_samples:{count}/{num_samples}, total:{total}\n------')

    # Display the final accumulated results
    print(f'Total added probability: {total}% / Count: {count}')
    print(f'Mean probability: {total/num_samples:.2f}%')
