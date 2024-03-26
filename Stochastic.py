import yfinance as yf
import pandas as pd
import datetime

#this is the Stochastic Oscillator Technical indicator and this helps when the market is trading sideways

class Stochastic():
    
    def __init__(self, ticker, start_date, period):
        self.ticker = ticker
        
        self.start_date = start_date
        
        self.period = period
        
        
    def find_ticker_data(self):
        data = yf.download(self.ticker, self.start_date, self.start_date - self.period)
        return data
        
    def find_highest_in_period(self):
        
        
    def find_lowest_in_period(self):
        
        
    def stochastic_oscillator(self):
        most_recent_close = 0
        so = ((most_recent_close - self.find_lowest_in_period)/(self.find_highest_in_period - self.find_lowest_in_period)) * 100
        return so