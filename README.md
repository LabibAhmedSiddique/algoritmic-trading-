# StockTrader Class Documentation

## Overview

The `StockTrader` class represents a simple trading strategy based on the concept of golden crosses and golden death cross in algorithmic trading technical analysis. It allows users to simulate buying and selling stocks using historical market data via analyzing the short term and long term moving average.

## Attributes

- `symbol`: str
  - The symbol of the stock to be traded.
- `from_date`: str
  - The start date of the historical data to be considered. Required format `YYYY-MM-DD`
- `to_date`: str
  - The end date of the historical data to be considered.Required format `YYYY-MM-DD`
- `has_position`: bool
  - A flag to track whether a position (buy/sell order) is currently open. Initialized to `False`
 - `initial_budget`: int
	  - Users initial budget. Default value is set to 5000

## Methods

1. `__init__(symbol, from_date, to_date)`
   - Initializes a new instance of the StockTrader class with the specified stock symbol, start date, and end date.

2. `get_data()`
   - Downloads historical market data for the specified stock symbol within the specified date range using the yfinance library.

3. `clean_data()`
   - Cleans the downloaded data by removing duplicate data points and handling `NaN` values using forward filling.

4. `calculate_moving_avg()`
   - Computes the 50-day and 200-day moving averages (MA50 and MA200) based on the closing prices of the stock.

5. `identify_golden_cross()`
   - Identifies golden crosses, which occur when the 50-day moving average crosses above the 200-day moving average, signaling a potential bullish trend.

6. `get_buy_quantity()`
   - Determines the quantity of shares to buy based on a fixed budget ($5000 by default) and the closing price of the stock at the first identified golden cross.

7. `buy()`
   - Executes a buy order if no position is currently open and a golden cross is identified. Records the buy date and the quantity of shares bought.

8. `identify_golden_cross_reversal()`
   - Identifies potential reversals of the golden cross, which occur when the 50-day moving average crosses below the 200-day moving average, signaling a potential bearish trend.

9. `sell()`
   - Executes a sell order if a position is currently open. If a reversal of the golden cross is identified, sells the shares immediately; otherwise, sells the shares on the last available date.

10. `evaluate()`
    - Calculates the profit or loss based on the difference between the selling price and the buying price of the shares.
 ## Installation 
 ### Project Setup

Clone the repository to your local machine using the following   
 command:

   

    https://github.com/LabibAhmedSiddique/algoritmic-trading-.git 
    
   get into to the project directory using the following command

 

    cd algoritmic-trading-

create a python virtual environment 

     python -m venv eval_test

Now activate the virtual environment with the following command 


    eval_test/Scripts/activate
after you activate the virtual environment run the `requirements.txt` file to install all the dependencies . To do so run the following command 

     pip install -r requirements.txt

### Run the project
Now inside terminal run the `app.py` file using the following command



## Example Usage

```python
# Initialize StockTrader instance
trader = StockTrader("AAPL", "2018-01-01", "2023-12-31")

# Download historical market data and clean it
trader.get_data()
trader.clean_data()

# Compute moving averages and identify golden crosses
trader.calculate_ma()
trader.identify_golden_cross()

# Buy shares based on identified golden crosses
trader.buy()

# Check for reversal after buy and sell accordingly
trader.identify_golden_cross_reversal()
trader.sell()

# Evaluate profit or loss
trader.evaluate()
```
## Reference 
[yfinance](https://pypi.org/project/yfinance/):Download market data from Yahoo! Finance API
