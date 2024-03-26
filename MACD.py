import math
import pandas as pd
import yfinance as yf
import datetime
from datetime import date
yf.pdr_override()
def calculateMACD(ticker) -> pd.DataFrame:
    today = datetime.date.today
    if today.weekday() == 5:
        today = today.replace(day = today - 1)
    elif today.weekday() > 0 != True:
        today = today.replace(day = today + 1)
    start_ema_12 = today.replace(day = today.day - 12)
    start_ema_26 = today.replace(day = today.day - 26 )
    ema_26_data = pdr.get_data_yahoo(ticker, start = start_ema_26.isoformat(), end = today.isoformat())
    ema_12_data = pdr.get_data_yahoo(ticker, start = start_ema_12.isoformat(), end = today.isoformat())
   