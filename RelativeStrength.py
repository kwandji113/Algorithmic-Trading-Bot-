import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


#this is a mathematical algorythm that will output the RSI for certain periods. This will calculate the RSI, 
#then over a certain period predict where the overbought and oversold values will be
#oversold = 30 or below
#overbought = 70 or above

class RelativeStrength():
    
    def __init__(self, ticker, end_date, period) -> None:
        self.end_date = end_date #could be current day or for testing days in the past
        self.period = period #this is going to be a number of days, for example 14 would be 14 days of stock market open days
        self.ticker = ticker #this is the stock symbol
        self.total_period = 2 * period
        
    
    def find_ticker_data(self):
        date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
        start_date = date_obj - timedelta(days = self.period)
        data = yf.download(self.ticker, start_date, self.end_date)
        return data
    
    def find_gain(self, period):
        #this takes the amount of green days, calculate the average gain over the period
        closing_prices = self.find_ticker_data()['Close']
        gains = []
         
        for i in range(len(closing_prices)):
            j = i + 1
            if j < len(closing_prices):                
                difference =  ((closing_prices[j]-closing_prices[i])/closing_prices[i]) * 100
            elif j == len(closing_prices):
                difference = 0.0
             
            
            if difference >= 0.0:
                gains.append(abs(difference))
            elif difference < 0.0:
                gains.append(0.0)
        print(gains)
        avg_gain = sum(gains) / self.period
        return avg_gain
    
    def find_loss(self, period):
        #this finds avg loss over period
        closing_prices = self.find_ticker_data()['Close']
        print(closing_prices)
        losses = []
        
        for i in range(len(closing_prices)):
            j = i + 1
            if j < len(closing_prices):                
                difference = ((closing_prices[j]-closing_prices[i])/closing_prices[i]) * 100
            elif j == len(closing_prices):
                difference = 0.0
                
            if difference <= 0.0:
                losses.append(abs(difference))
            elif difference > 0.0:
                losses.append(0.0)
        
        avg_loss = sum(losses) / self.period
        return avg_loss
    
    def rsi(self): 
        gain = self.find_gain(self.period)
        loss = self.find_loss(self.period)
        gain_over_loss = gain / loss
        rsi = 100.0 - (100.0 / (1.0 + gain_over_loss))
        return rsi

#testing:
# rsi_obj = RelativeStrength('AAPL','2021-02-06', 14)
# rsi_value = rsi_obj.rsi()
# print(rsi_value)