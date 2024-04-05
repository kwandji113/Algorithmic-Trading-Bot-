import math
import numpy as np
import pandas as pd
import yfinance as yf
import datetime
from datetime import datetime, timedelta

#calculate a n-day exponential moving average
def nDaySMA(stock_symbol,start_date,end_date) -> int:
    calc_end_date = datetime.fromisoformat(end_date)
    calc_end_date += timedelta(days = 1)
    end_date = calc_end_date.strftime('%Y-%m-%d')
    history = yf.download(stock_symbol,start_date,end_date)
    print(history)
    #create a list with every date from the start date to the end date, ignorning weekends(holidays will be automatically avoided) 
    dates = get_weekdays(start_date,end_date) #df_adj = np.array(df_yf["Close"])
    close_prices = []
    for day in dates: 
        try:
            close_prices.append((day,history['Close'].loc[day]))
        except KeyError:
            print(F" Stock market is not open on '{day}'")

        
    intial_ema = 0.0 #will calculate the sma for the first 12 and 26 day period 
    sma_26 = 0.0
    consequent_emas = []
    consequent_emas_26 =[]
    alpha_12 = 2/12+1
    alpha_26 = 2/26+1

    counter_12 = 0
    counter_26 = 0
    
    for i in range(13):
        intial_ema += close_prices[i][1]
    
    calc_ema = intial_ema
    for i in range(13,26):
        next_ema = (close_prices[i][1] * alpha_12) + calc_ema * (1-alpha_12)
        consequent_emas.append(next_ema)
        calc_ema = next_ema
    #EMAtoday = (price today - EMA yesterday) X alpha + EMAyesterday
        
    
    for i in range(27):
        sma_26 += close_prices[i][1]
    calc_ema_26 = sma_26
    for i in range(27,57):
        next_ema = (close_prices[i][1] * alpha_26) + calc_ema_26 * (1-alpha_26)
        consequent_emas_26.append(next_ema)
        calc_ema_26 = next_ema
    

    return [consequent_emas[-1],consequent_emas_26[-1]]




def get_weekdays(start_date,end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    total_days = []
    while start_date <= end_date:
        if start_date.weekday() < 5:
            total_days.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=1)
    total_days.pop()
    return total_days

def nDayEMA(stock_symbol,cur_day): #period is fixed to 12 and 26 days
    cur_day = datetime.fromisoformat(cur_day)
    if cur_day.weekday() == 6:
        cur_day += timedelta(days=1)
    elif cur_day.weekday() == 5:
        cur_day-=timedelta(day=1)
    
    start_date = cur_day - timedelta(days=55*1.5)
    if start_date.weekday() == 6:
        start_date += timedelta(days=1)
    elif cur_day.weekday() == 5:
        start_date-=timedelta(day=1)
    
    return nDaySMA(stock_symbol,start_date.strftime('%Y-%m-%d'),cur_day.strftime('%Y-%m-%d'))

    



