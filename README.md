# Demystifying Doji

The Doji candlestick pattern has long fascinated traders and analysts. 

Characterized by virtually identical opening and closing prices, the Doji's shadows may vary in length, and its appearance often sparks debates about potential market reversals. 

But how effective is the Doji in signaling such reversals? This investigation seeks to unravel the truth.

# Definition of Doji

It is a doji candle if `price(close) - price(open) == 0`

A Doji candle is formed when the difference between the closing and opening prices is zero.

![image](https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/387755bb-fd59-46e3-98ed-bd27cd17c0e0)

image source - [nasdaq.com](https://www.nasdaq.com/articles/hammer-doji-bullish-reversal-candlestick-patterns-2017-01-03)


# Objective

The primary goal of this study is to investigate the efficacy of the Doji pattern in signaling a reversal in trend. 

By examining various market scenarios, we aim to determine whether the appearance of a Doji truly shows a change in market direction.

# Observations

## SPY (S&P 500 ETF) - Daily Data 

### Test period: 2013.08.23 ~ 2023.08.22

The analysis of SPY reveals a probability of trend change after a Doji appearance of 54.55% (6 out of 11 instances). 

The visual representation of these instances can be found below:

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2014-08-26 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/79c589fb-9a1b-4375-9b3f-303e26af8d52"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/4e82c901-17a7-4adb-a20e-172a91bcd9d1"> | TRUE |
| 2015-05-15 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/0041145f-5284-411a-9496-fd11ee19e285"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/d47ec329-4172-4df7-b859-d4f94f262719"> | TRUE |
| 2015-06-09 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/5dd96819-2f89-4f9d-8d2e-822aeb06e9bc"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/82d93d30-85a4-4bfa-a0da-c067163aec68"> | FALSE |
| 2015-06-17 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/5e9de690-22d4-45df-bf47-2896e5d50d8d"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/b02cce2a-f80c-46a9-9762-50444feb9846"> | FALSE        |
| 2017-05-01 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/a4326246-2ff5-4ff9-a86e-23a159f949c8"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/0a780fae-0ab9-4645-a6d8-1fa6225618cf"> | FALSE        |
| 2018-05-25 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/8829e095-b4d4-461c-88d0-931754361557"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/102a10f4-3c52-4881-ac33-0a5dd5c9ceb4"> | FALSE        |
| 2018-10-02 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/4562c387-9373-4f04-afb0-9f538b09e6ab"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/9688c18e-f97c-4236-92ee-b4167990f8e0"> | TRUE         |
| 2019-05-08 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/09e07aeb-11c2-495a-a208-7fb2dc2c3514"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/1e905041-286f-4ccd-ba71-e65d81ecd2f5"> | TRUE         |
| 2019-06-14 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/62c0bd72-aa12-43d3-984f-b5239fd80592"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/f520e9b8-3c75-43ff-ad68-760fb2bb88b0"> | FALSE        |
| 2020-11-02 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/41bbd23c-daf1-4987-bc60-6e6c3a529fbd"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/9890e40b-cf7b-465b-aec5-f19b51e52e71"> | TRUE         |
| 2021-08-24 | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/0c47b1a1-9c43-4267-81e2-65193ce30e90"> | <img width="400" src="https://github.com/kjs29/demystify-doji-candlestick/assets/96529477/88202f16-f52f-4806-9385-737ba52439fd"> | TRUE         |

**Margin Of Error(MOE) = 0%. [^1]**

**R_before_Doji and R_after_Doji are derivated from 20 trading days.**

## QQQ (NASDAQ-100 ETF) - Daily Data 

### Test period: 2013.08.26 ~ 2023.08.22

For QQQ, the probability of trend change following a Doji is 29.41%. 

The detailed observations are as follows:

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2013-12-09 |       0.909888 |      0.717477 |        False |
| 2014-02-12 |      -0.414075 |      0.360623 |         True |
| 2014-11-04 |       0.684007 |      0.966447 |        False |
| 2014-11-25 |       0.966791 |     -0.500820 |         True |
| 2015-01-26 |      -0.405235 |      0.974566 |         True |
| 2015-06-22 |      -0.432752 |      0.508323 |         True |
| 2016-06-08 |       0.860118 |     -0.277862 |         True |
| 2016-12-06 |       0.241883 |      0.378632 |        False |
| 2017-01-17 |       0.710802 |      0.937530 |        False |
| 2017-01-27 |       0.937262 |      0.981065 |        False |
| 2017-05-10 |       0.969708 |      0.892039 |        False |
| 2017-08-04 |       0.782253 |      0.180834 |        False |
| 2017-08-28 |      -0.504303 |     -0.214864 |        False |
| 2017-11-14 |       0.882556 |      0.148962 |        False |
| 2018-06-15 |       0.951446 |      0.387703 |        False |
| 2018-08-30 |       0.556564 |      0.220182 |        False |
| 2019-06-21 |       0.813423 |      0.832825 |        False |

### Test period: 02/27/2014 ~ 08/18/2016

Probability of trend change after a doji appearance: 80.00%

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2014-11-04 |      0.684007 |     0.966447 |        False |
| 2014-11-25 |      0.966791 |    -0.500820 |         True |
| 2015-01-26 |     -0.405235 |     0.974566 |         True |
| 2015-06-22 |     -0.432752 |     0.508323 |         True |
| 2016-06-08 |      0.860118 |    -0.277862 |         True |


## GLD (Gold ETF) - Daily Data

### Test period: 2013.08.26 ~ 2023.08.22

In the case of GLD, the Doji pattern appears to have a stronger correlation with trend changes, with a probability of 63.64%.

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2014-05-15 |       0.172831 |     -0.597069 |         True |
| 2016-09-22 |      -0.040200 |     -0.833573 |        False |
| 2016-10-03 |      -0.293298 |      0.639560 |         True |
| 2016-10-10 |      -0.638546 |      0.888980 |         True |
| 2018-02-26 |      -0.212621 |      0.466576 |         True |
| 2018-04-23 |       0.216691 |     -0.771676 |         True |
| 2018-12-27 |       0.908018 |      0.351492 |        False |
| 2019-03-04 |       0.190813 |      0.304051 |        False |
| 2021-01-05 |       0.771963 |     -0.541814 |         True |
| 2021-11-23 |       0.748877 |      0.472644 |        False |
| 2022-07-15 |      -0.944289 |      0.953989 |         True |


## TLT (20-Year Treasury Bond ETF) - Daily Data (2013.08.26 ~ 2023.08.22)

The analysis of TLT yields a probability of trend change after a Doji appearance of 46.15%.

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2015-03-16 |      -0.336019 |     -0.270982 |        False |
| 2015-04-27 |      -0.624442 |     -0.742910 |        False |
| 2017-02-01 |      -0.519381 |      0.184155 |         True |
| 2017-05-15 |      -0.884289 |      0.758800 |         True |
| 2017-09-29 |      -0.766997 |     -0.289241 |        False |
| 2018-06-19 |       0.345815 |      0.716852 |        False |
| 2018-07-06 |       0.907663 |     -0.902788 |         True |
| 2018-07-16 |       0.886123 |     -0.500450 |         True |
| 2019-05-03 |      -0.179806 |      0.907775 |         True |
| 2020-02-12 |       0.792282 |      0.864004 |        False |
| 2020-04-14 |       0.624550 |     -0.800298 |         True |
| 2021-08-03 |       0.627635 |      0.238749 |        False |
| 2023-07-18 |      -0.686837 |     -0.941213 |        False |


## VNQ (Real Estate ETF) - Daily Data (2013.08.26 ~ 2023.08.22)

For VNQ, the probability of trend change following a Doji is exactly 50.00%.

| Doji_Date  | R_before_Doji | R_after_Doji | Trend_Change |
|------------|---------------|--------------|--------------|
| 2014-05-09 |       0.949691 |      0.713544 |        False |
| 2014-06-02 |       0.566969 |     -0.246980 |         True |
| 2014-07-15 |       0.565256 |     -0.758967 |         True |
| 2014-10-06 |      -0.888966 |      0.982454 |         True |
| 2014-11-28 |       0.186775 |      0.625628 |        False |
| 2014-12-18 |       0.669793 |      0.922071 |        False |
| 2017-03-01 |       0.937747 |     -0.464087 |         True |
| 2018-01-25 |      -0.816294 |     -0.763135 |        False |
| 2020-08-25 |      -0.138082 |     -0.542076 |        False |
| 2020-10-22 |       0.416971 |      0.879713 |        False |
| 2021-05-18 |      -0.370968 |      0.944490 |         True |
| 2021-11-29 |      -0.119019 |      0.878053 |         True |
| 2022-12-30 |      -0.819642 |      0.886157 |         True |
| 2023-01-19 |       0.807325 |      0.422902 |        False |


# Conclusion

<em>Probability of effectiveness of Doji's reversal</em>

|                   | SPY                  | QQQ                  | GLD                  | TLT                  | VNQ                  | AAPL                 | GOOG                 | MSFT                 | COST                 |
|-------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| Training Periods  | (08/23/2013 ~ 08/22/2023) | (08/26/2013 ~ 08/22/2023) | (08/26/2013 ~ 08/22/2023) | (08/26/2013 ~ 08/22/2023) | (08/26/2013 ~ 08/22/2023) | (08/26/2013 ~ 08/23/2023) | (03/27/2014 ~ 08/23/2023) | (08/26/2013 ~ 08/23/2023) | (08/26/2013 ~ 08/23/2023) |
| 5                 | 0.1818               | 0.5294               | 0.4167               | 0.3846               | 0.2857               | 0.3333               | 0.65                 | 0.6316               | 0.6667               |
| 10                | 0.6364               | 0.4118               | 0.5                  | 0.6923               | 0.7143               | 0.5417               | 0.5                  | 0.4211               | 0.3333               |
| 20                | 0.5455               | 0.2941               | 0.6364               | 0.4615               | 0.5                  | 0.375                | 0.4091               | 0.4211               | 0.5556               |
| 50                | 0.6364               | 0.4118               | 0.3636               | 0.4167               | 0.5                  | 0.3333               | 0.65                 | 0.3333               | 0.375                |


The Doji candlestick pattern does not present a consistent or strong correlation with trend reversals across various markets.

The probabilities observed range from as low as 29.41% to as high as 63.64%, indicating a lack of uniformity in its predictive power.

It is essential to recognize that correlation does not imply causation. While the Doji may coincide with trend changes in some instances, it does not necessarily cause them. Traders and investors should exercise caution when interpreting the Doji pattern. It seems wise to demystify the Doji pattern and not over-interpret it. That said, it doesn't mean that various other patterns incorporating Doji are meaningless. The pursuit of precise understanding through future quantitative research appears to be an essential approach, reflecting a commitment to rigorous analysis rather than superficial interpretation.

---
[^1]: Daily Close - Daily Open == 0. If MOE is 0.05%, abs(Daily Close - Daily Open) <= Daily Close * 0.05 / 100
<!-- In the complex and multifaceted world of financial markets, the Doji remains an enigmatic symbol, one that invites further exploration but defies simplistic interpretation. Its allure lies in its ambiguity, and its true value may be in the questions it prompts rather than the answers it provides. -->

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
