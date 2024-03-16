import math
import pandas as pd
import yfinance as yf
import datetime
import statistics as stat
    
def calculate_moving_average(stock_symbol, n_days, start_date, end_date):
    # Fetch historical market data
    data = yf.Ticker(stock_symbol)
    historical_data = data.history(start=start_date, end=end_date)
    starting_row_name = historical_data.iloc[0].name
    ending_row_name = historical_data.iloc[len(historical_data) - 1].name

    # Fetch relevant data to find moving average
    full_data = data.history(period="max")
    starting_index = full_data.index.get_loc(starting_row_name) - (n_days - 1) #+1 because the first days closing price is included in the calculation
    if(starting_index < 0):
        return None
    ending_index = full_data.index.get_loc(ending_row_name)
    dataList = full_data['Close'].tolist()[starting_index:ending_index + 1]
    #find moving average
    upper_index =  n_days - 1
    lower_index = 0
    moving_average = []
    while(upper_index < len(dataList)):
        moving_average.append(stat.mean(dataList[lower_index:upper_index]))
        upper_index += 1
        lower_index += 1
    return moving_average
    

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

#MACD


# Example usage:
stock_symbol = 'AAPL'  # Apple Inc.
n_days = 50
start_date = datetime.datetime(2024, 3, 5)
end_date = datetime.datetime(2024, 3, 6)

print(calculate_moving_average(stock_symbol, n_days, start_date, end_date))
thing = [1, 2, 3, 4]
print(thing[0:len(thing)])