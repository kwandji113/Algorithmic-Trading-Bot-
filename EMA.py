import math
import pandas as pd
import yfinance as yf
import datetime

#calculate a n-day exponential moving average
def nDayEMA(stock_symbol, n_days, start_date, end_date):
    data = yf.Ticker(stock_symbol)
    
    historical_data = data.history("max")
    if historical_data.empty:
        return None

    # Calculate Exponential Moving Average (EMA)
    ema = historical_data['Close'].ewm(span=n_days, adjust=False).mean()
    
    return ema

def MACD(stock_symbol):
    pass

ema = nDayEMA('AAPL', 20, '2024-01-01', '2024-03-01')
print(ema)