import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

#this is the Stochastic Oscillator Technical indicator and this helps when the market is trading sideways
#or any other ways, just an alternate use and indicator for long and short term trading

class Stochastic():
    
    def __init__(self, ticker, start_date, period):
        self.ticker = ticker
        
        self.start_date = start_date
        
        self.period = period
               
        
    def find_ticker_data(self):
        date_obj = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = date_obj - timedelta(days = self.period)
        data = yf.download(self.ticker, self.start_date, end_date)
        return data
        
    def find_highest_in_period(self):
        data = self.find_ticker_data()
        highest = -1 #because a stock value cannot be less than -1, so itll never be the lowest value
        for val in  data['High']:
            if val > highest:
                highest = val
        
        return highest
        
    def find_lowest_in_period(self):
        data = self.find_ticker_data()
        lowest = float('inf') #because a stock value cannot be more than infinity , so itll never be the lowest value
        for val in  data['High']:
            if val < lowest:
                lowest = val
        
        return lowest
        
    def stochastic_oscillator(self):
        data = self.find_ticker_data()
        most_recent_close = data['Close'].iloc[-1]
        #iloc stands for integer location, specifically for a pandas dataframa and can find a value at index (-1 for the end of the frame)
        so = ((most_recent_close - self.find_lowest_in_period)/(self.find_highest_in_period - self.find_lowest_in_period)) * 100
        return so