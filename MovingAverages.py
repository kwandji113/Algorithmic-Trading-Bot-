import math
import pandas as pd
import yfinance as yf
import datetime
import statistics as stat
    
def calculate_moving_average(stock_symbol, n_days, start_date, end_date):
    data = yf.Ticker(stock_symbol) #get the stock data
    historical_data = data.history(start=start_date, end=end_date) #get the data from start date to end date, to get the indexes
    
    if historical_data.empty:
        return None

    starting_row_name = historical_data.iloc[0].name
    ending_row_name = historical_data.iloc[-1].name

    full_data = data.history(period="max")
    
    starting_index = full_data.index.get_loc(starting_row_name) - (n_days - 1) #find our desired position in the max dataframe
    ending_index = full_data.index.get_loc(ending_row_name) #find our end_date in the max dataframe

    if starting_index < 0: #prevent out of bound errors
        return None
    relevant_data = full_data.iloc[starting_index:ending_index + 1]
    moving_averages = relevant_data['Close'].rolling(window=n_days).mean().to_frame()
    aligned_moving_averages = moving_averages.loc[starting_row_name:ending_row_name]

    return aligned_moving_averages


#calculate a n-day exponential moving average
def nDayEMA(stock_symbol, n_days, start_date, end_date):
     # Fetch historical market data
    data = yf.Ticker(stock_symbol)
    historical_data = data.history(start=start_date, end=end_date)
    starting_row_name = historical_data.iloc[0].name
    ending_row_name = historical_data.iloc[len(historical_data) - 1].name

    # Fetch relevant data to find moving average
    full_data = data.history(period="max")
    starting_index = full_data.index.get_loc(starting_row_name) - 1
    ending_index = full_data.index.get_loc(ending_row_name)

    dataList = full_data['Close'].tolist()[starting_index:ending_index]
    k = 2.0 / (n_days + 1)
    yesterdays_ema = dataList[0]
    print(yesterdays_ema)
    
    ema = []
    first = True
    for price in dataList:
        if(first):
            first = False
            break
        print(price)
        new_ema = (price - yesterdays_ema) * k + yesterdays_ema
        ema.append(new_ema)
        yesterdays_ema = new_ema
    return ema
        
        
    


#calculate a golden cross between a s-day moving average, and a l-day moving average
def goldenCross(short, long):
    pass

moving_average = calculate_moving_average('AAPL', 20, '2023-01-01', '2023-03-01')
print(moving_average)
