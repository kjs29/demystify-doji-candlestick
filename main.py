import random
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
from correlation_analysis import calculate_correlation_coefficients
from data_preparation import add_doji_column, remove_non_numeric_symbols
from data_visualization import create_dataframe, draw_linear_regression

def main(filename, training_days=20, test_different_time=False):
    # Import dataset
    df = pd.read_csv(filename)

    # Rename a column name
    df.rename(columns={'Close/Last': 'Close'}, inplace=True)

    # randomly choose rows
    if test_different_time:
        starting_index = random.randint(0,len(df)-2)
        ending_index = random.randint(starting_index+1, len(df)-1)
        df = df.iloc[starting_index: ending_index]
    training_date_begin = df.iloc[len(df)-1]['Date']
    training_date_end = df.iloc[0]['Date']

    # get rid of non-numeric symbols in the columns and convert to float type
    cols = ['Close','Open','High','Low']
    remove_non_numeric_symbols(df, cols)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort the DataFrame by the 'Date' column in ascending order
    df = df.sort_values(by='Date', ascending=True)

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Add 'doji' column
    add_doji_column(df,error_margin_percentage=0)

    # Calculate correlation coefficient
    calculate_correlation_coefficients(df, training_days, future=False)
    calculate_correlation_coefficients(df, training_days, future=True)

    # Create a new DataFrame 'doji' and save it
    doji = df[df['doji']==True]
    doji.to_csv('doji.csv')

    # Save images
    for i in doji.index:
        past_dates = df.iloc[i][f'past_{training_days}_dates']
        draw_linear_regression(past_dates, df.iloc[i][f'past_{training_days}_days'])
        plt.savefig(f'pictures/past_{training_days}_days_{i}.png')
        plt.close()

        future_dates = df.iloc[i][f'future_{training_days}_dates']
        draw_linear_regression(future_dates, df.iloc[i][f'future_{training_days}_days'])
        plt.savefig(f'pictures/future_{training_days}_days_{i}.png')
        plt.close()

    # Create new dataframe
    snapshot_df = create_dataframe(doji, training_days)

    # save the snapshot_df as image file
    dfi.export(snapshot_df, f'result_{count}.png')

    trend_change_row = snapshot_df[snapshot_df['Trend_Change']==True]

    print(f'### Test period({count}): {training_date_begin} ~ {training_date_end}')

    try:
        probability_of_doji_reversal = round(len(trend_change_row)/len(snapshot_df)*100,4)
        print(f"Probability of trend change after a doji appearance: {probability_of_doji_reversal}%")
        snapshot_df.to_csv('Result_' + filename)
        return probability_of_doji_reversal
    
    except ZeroDivisionError:
        print(f"There is no doji appearance.\n")
        return None


# Run the main function 'num_samples' times, accumulating the results only when there is a doji appearance.
total = 0
count = 0
num_samples = 1
filename = 'HistoricalData_COST_from_Nasdaq.csv'

while count < num_samples:
    result = main(filename, 50)
    if result is not None:
        total += result
        count += 1
    print(f"count/total_num_samples:{count}/{num_samples}, total:{total}\n------")

print(f"total:{total}")
print(f"count:{count}")
print(f"final:{total/num_samples:.2f}")
