# Demystifying Doji

Doji candle is formed when opening and closing prices are virtually the same. The lengths of shadows can vary. If previous are bearish, after a Doji, may be ready to bullish.

# Definition of Doji

It is a doji candle if `price(close) - price(open) == 0`

<!-- plan.
1. Define doji
2. Define uptrend, and downtrend
    a. Linear regression model
3. Calculate the empirical probability of 'likelyhood of doji candle's reversal after downtrend'
    a. if downtrend period is 10, calculate 10 days later
    b. if downtrend period is 5, calculate 5 days later
4. Calculate the empirical probability of 'likelyhood of doji candle's reversal after uptrend'
    a. if uptrend period is 10, calculate 10 days later
    b. if uptrend period is 5, calculate 5 days later
5. Visualize scatterplot
    a.https://realpython.com/visualizing-python-plt-scatter/ -->


<!-- Mismatched Column Names: Ensure that the column names used throughout the code match the column names in the CSV file exactly. Any difference in naming could lead to a KeyError.

Lack of Error Handling: If there are missing values (e.g., NaN) in the 'Close' or 'Open' columns, some of the calculations might produce unexpected results. You might consider handling or filling missing values appropriately.

Complexity of the Code: The code has multiple nested functions, which can make debugging more challenging. Consider breaking the code down into smaller, testable units and validating each piece individually.

Date Sorting Issue: If the dates in your CSV file are not sorted in ascending order, the shift operation and other temporal calculations might not behave as expected. Your code snippet already sorts by date, but make sure the CSV's date format is recognized correctly by pd.to_datetime.

Lambda Function for Doji: The equality check for the 'Close' and 'Open' prices (row['Close'] == row['Open']) might be too strict if these are floating-point numbers. You might consider a tolerance level to account for minor differences (e.g., abs(row['Close'] - row['Open']) < tolerance).

Correlation Coefficient Calculation: The calculation seems complex, and it might be beneficial to test it with known values to ensure it's working as expected. Consider using built-in functions like NumPy's np.corrcoef to calculate the correlation coefficient, as this could simplify the code and reduce the likelihood of errors.

Testing Different Parts of the Code: Start by testing smaller parts of the code independently. You could print or log intermediate variables to ensure they are what you expect. Debugging in smaller steps can help you identify where the problem might be. -->
