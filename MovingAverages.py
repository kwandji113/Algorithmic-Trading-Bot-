import math
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
    
class MovingAverages():

    def __init__(self, ticker):
        self.ticker = ticker

    
    def calculate_moving_average(self, n_days, start_date, end_date) -> pd.DataFrame:
        adjusted_start_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=n_days * 1.5)).strftime('%Y-%m-%d') #add a buffer since the stock market isn't open everyday
        historical_data = yf.download(self.ticker, adjusted_start_date, end_date)
        #get the data from start date to end date, to get the indexes
        if historical_data.empty:
            return None
        
        moving_averages = historical_data['Close'].rolling(window=n_days).mean().to_frame()
        aligned_moving_averages = moving_averages.loc[start_date:]

        return aligned_moving_averages

#testing:
# ma_object = MovingAverages('AAPL')
# moving_average = ma_object.calculate_moving_average(20, '2023-01-06', '2023-03-04')
# moving_average2 = ma_object.calculate_moving_average(50, '2024-01-01', '2024-03-04')
# print(moving_average2)