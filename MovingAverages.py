import math
import pandas as pd
import yfinance as yf
import datetime

#calculate n day moving avreage
def calculate_moving_average(stock_symbol, n_days, start_date, end_date):
    # Fetch historical market data
    data = yf.Ticker(stock_symbol)
    historical_data = data.history(start=start_date, end=end_date)
    starting_row_name = historical_data.iloc[0].name
    ending_row_name = historical_data.iloc[len(historical_data) - 1].name

    full_data = data.history(period="max")
    starting_index = full_data.index.get_loc(starting_row_name) - n_days
    if(starting_index < 0):
        return None
    ending_index = full_data.index.get_loc(ending_row_name)
    dataList = full_data['Close'].tolist()[starting_index:ending_index]
    return dataList


    
    #get the first value of the historical data dataframe
    #then get the max data frame and find that value in the dataframe, go back n rows, and then we start
    
    

#calculate a n-day exponential moving average
def nDayEMA(days, start, end):
    pass


#calculate a golden cross between a s-day moving average, and a l-day moving average
def goldenCross(short, long):
    pass

#MACD


# Example usage:
stock_symbol = 'AAPL'  # Apple Inc.
n_days = 50
start_date = datetime.datetime(2024, 3, 5)
end_date = datetime.datetime(2024, 3, 13)

print(calculate_moving_average(stock_symbol, n_days, start_date, end_date))