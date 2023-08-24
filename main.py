import pandas as pd
import matplotlib.pyplot as plt
from correlation_analysis import calculate_correlation_coefficients
from data_preparation import add_doji_column
from data_visualization import create_dataframe, draw_linear_regression

# Import SPY.csv
df = pd.read_csv('HistoricalData_VNQ_from_Nasdaq.csv')

# Rename a column name
df.rename(columns={'Close/Last': 'Close'}, inplace=True)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by the 'Date' column in ascending order
df = df.sort_values(by='Date', ascending=True)

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Add 'doji' column
add_doji_column(df,error_margin_percentage=0)

# Calculate correlation coefficient
calculate_correlation_coefficients(df, num_days=20, future=False)
calculate_correlation_coefficients(df, num_days=20, future=True)

# Create a new DataFrame 'doji' and save it
doji = df[df['doji']==True]
doji.to_csv('doji.csv')

# Save images
for i in doji.index:
    past_dates = df.iloc[i]['past_20_dates']
    draw_linear_regression(past_dates, df.iloc[i]['past_20_days'])
    plt.savefig(f'pictures/past_20_days_{i}.png')
    plt.close()

    future_dates = df.iloc[i]['future_20_dates']
    draw_linear_regression(future_dates, df.iloc[i]['future_20_days'])
    plt.savefig(f'pictures/future_20_days_{i}.png')
    plt.close()

# Create new dataframe
snapshot_df = create_dataframe(doji, 20)

print(snapshot_df)

trend_change_row = snapshot_df[snapshot_df['Trend_Change']==True]

print(f"Probability of trend change after a doji appearance: {len(trend_change_row)/len(snapshot_df)*100:.2f}%")
snapshot_df.to_csv('VNQ_20130826_20230822.csv')
