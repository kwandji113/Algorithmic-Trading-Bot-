import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


#this is a mathematical algorythm that will output the RSI for certain periods. This will calculate the RSI, 
#then over a certain period predict where the overbought and oversold values will be
#oversold = 30 or below
#overbought = 70 or above

class RelativeStrength():
    
    def __init__(self, ticker, end_date, period, window) -> None:
        self.end_date = end_date #could be current day or for testing days in the past
        self.period = period #this is going to be a number of days, for example 14 would be 14 days of stock market open days
        self.ticker = ticker #this is the stock symbol
        self.window = window # for the week before, see getOpinion.py for more information
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
    
    def find_gain(self, start):
        #this takes the amount of green days, calculate the average gain over the period
        closing_prices = self.data['Close']
        gains = []
         
        for i in range(self.window - start, len(closing_prices) - start):
            j = i + 1
            if j < len(closing_prices):                
                difference =  ((closing_prices[j]-closing_prices[i])/closing_prices[i]) * 100
            elif j == len(closing_prices):
                difference = 0.0
             
            
            if difference >= 0.0:
                gains.append(abs(difference))
            elif difference < 0.0:
                gains.append(0.0)
                
        avg_gain = sum(gains) / self.period
        return avg_gain
    
    def find_loss(self,start):
        #this finds avg loss over period
        closing_prices = self.data['Close']
        losses = []
        
        for i in range(self.window - start, len(closing_prices) - start):
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
    
    def rsi(self, start): 
        gain = self.find_gain(start)
        loss = self.find_loss(start)
        gain_over_loss = gain / loss
        rsi = 100.0 - (100.0 / (1.0 + gain_over_loss))
        return rsi
    
    def find_rsi_range(self):
        rsi_for_window = []
        for i in range(self.window):
            rsi_val = self.rsi(i)
            rsi_for_window.append(rsi_val)
            
        
        return rsi_for_window
        

#testing:
# rsi_obj = RelativeStrength('AAPL','2021-02-06', 14, 7)
# rsi_list = rsi_obj.find_rsi_range()
# print(rsi_list)