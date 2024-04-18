import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

#this is the Stochastic Oscillator Technical indicator and this helps when the market is trading sideways
#or any other ways, just an alternate use and indicator for long and short term trading

class Stochastic():
    
    def __init__(self, ticker, end_date, period):
        self.ticker = ticker
        
        self.end_date = end_date
        
        self.period = period
        
        self.data = self.find_ticker_data()
               
        
    def find_ticker_data(self):
        date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
        start_date = date_obj - timedelta(days = self.period)
        data = yf.download(self.ticker, start_date, self.end_date)
        return data
        
    def find_highest_in_period(self):
        highest = -1 #because a stock value cannot be less than -1, so itll never be the lowest value
        for val in  self.data['High']:
            if val > highest:
                highest = val
        
        return highest
        
    def find_lowest_in_period(self):
        lowest = float('inf') #because a stock value cannot be more than infinity , so itll never be the lowest value
        for val in  self.data['Low']:
            if val < lowest:
                lowest = val
        
        return lowest
        
    def stochastic_oscillator(self):
        most_recent_close = self.data['Close'][-1]
        lowest = self.find_lowest_in_period()
        highest = self.find_highest_in_period()
        so = ((most_recent_close - lowest)/(highest - lowest)) * 100
        return so

#testing: 
# stoch = Stochastic('AAPL', '2021-02-06', 14)
# print(stoch.data)
# high = stoch.find_highest_in_period()
# low = stoch.find_lowest_in_period()
# so = stoch.stochastic_oscillator()
# print(so)