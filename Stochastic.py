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
        
        self.window = 7
        
        self.data = self.find_ticker_data()
               
        
    def find_ticker_data(self):
        date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
        #coming loop will find weekdays vs weekends to find a real 14 day period of stock market days
        num_subtract = 0
        num_days = 0
        while num_days != 14:
            current_day = date_obj - timedelta(days = num_subtract)
            day_name = current_day.strftime("%A")
            
            if day_name == 'Saturday' or day_name == 'Sunday':
                num_subtract += 1
            else: 
                num_days += 1
                num_subtract += 1
               
        start_date = date_obj - timedelta(days = num_subtract + self.window)
        data = yf.download(self.ticker, start_date, self.end_date)
        return data
        
    def find_highest_in_period(self, start):
        highest = -1 #because a stock value cannot be less than -1, so itll never be the lowest value
        for i in range(self.window - start, len(self.data['High'])- start):
            if self.data['High'][i] > highest:
                highest = self.data['High'][i]
        
        return highest
        
    def find_lowest_in_period(self, start):
        lowest = float('inf') #because a stock value cannot be more than infinity , so itll never be the lowest value
        for i in range(self.window - start, len(self.data['Low'])- start):
            if self.data['Low'][i] < lowest:
                lowest = self.data['Low'][i]
        
        return lowest
        
    def stochastic_oscillator(self, start):
        most_recent_close = self.data['Close'][-1]
        lowest = self.find_lowest_in_period(start)
        highest = self.find_highest_in_period(start)
        so = ((most_recent_close - lowest)/(highest - lowest)) * 100
        return so
    
    def stoch_list(self):
        so_list = []
        for i in range(self.window):
            so_val = self.stochastic_oscillator(i)
            so_list.append(so_val)
            
            
#testing: 
# stoch = Stochastic('AAPL', '2021-02-06', 14, 7)
# print(stoch.data)
# so = stoch.stochastic_oscillator()
# print(so)