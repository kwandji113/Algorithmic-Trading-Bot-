import yfinance as yf
import pandas as pd
import datetime


#this is a mathematical algorythm that will output the RSI for certain periods. This will calculate the RSI, 
#then over a certain period predict where the overbought and oversold values will be
#oversold = 30 or below
#overbought = 70 or above

class RelativeStrength():
    
    def __init__(self, ticker, start_date, period) -> None:
        self.start_date = start_date #could be current day or for testing days in the past
        self.period = period #this is going to be a number of days, for example 14 would be 14 days of stock market open days
        self.ticker = ticker #this is the stock symbol
    
    def find_ticker_data(self):
        data = yf.download(self.ticker, self.start_date, self.start_date - self.period)
        return data
    
    def find_gain(self, period):
        #this takes the amount of green days, calculate the average gain over the period
        delta = self.find_ticker_data()['Close'].diff() 
        gain = (delta.where(delta > 0, 0)).rolling(period).mean()
        return gain
    
    def find_loss(self, period):
        #this finds avg loss over period
        delta = self.find_ticker_data()['Close'].diff()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        return loss
    
    def rsi(self, gain, loss): 
        gain = self.find_gain(self.period)
        loss = self.find_loss(self.period)
        gain_over_loss = gain / loss
        rsi = 100 - (100 / (1 + gain_over_loss))
        return rsi