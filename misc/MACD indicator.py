import math
import EMA_Function 
from EMA_Function import nDayEMA as EMA
import sys
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
from datetime import date
yf.pdr_override()
def calculateMACD(ticker) -> pd.DataFrame:
    today = datetime.date.today()
    if today.weekday() == 5:
        today = today.replace(day = today - 1)
    elif today.weekday() == 6:
        today = today.replace(day = today + 1)
    
    ema_values = EMA(ticker,today.strftime('%Y-%m-%d'))
    macd = (ema_values[0] - ema_values[1])
    return macd


calculateMACD('MSFT')