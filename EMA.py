import math
import pandas as pd
import yfinance as yf
import datetime
from datetime import datetime, timedelta

#calculate a n-day exponential moving average
def nDayEMA(stock_symbol, n_days, start_date, end_date):
    adjusted_start_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=n_days * 1.5)).strftime('%Y-%m-%d') #add a buffer since the stock market isn't open everyday
    historical_data = yf.download(stock_symbol, adjusted_start_date, end_date)
    
    if historical_data.empty:
        return None

    # Calculate Exponential Moving Average (EMA)
    ema = historical_data['Close'].ewm(span=n_days, adjust=False).mean()
    
    aligned_ema = ema.loc[start_date:]

    return aligned_ema

ema = nDayEMA('AAPL', 20, '2024-01-01', '2024-03-01')
print(ema)