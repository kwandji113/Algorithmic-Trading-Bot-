import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import RelativeStrength
import Stochastic

#this program is going to take Technical Analysis algorythms and create an opinion purely based on the numbers they return
#example: RSI safe values range from 30-70. If the number returned is 30, then goes up, it is a buy signal

class GetOpinion():
    
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.today = datetime.today().strftime('%Y-%m-%d') #returns todays date
        self.period = 14
        self.window = 7 #for the week before
        

    def form_opinion(self):
        #1 = buy, -1 = sell, 0 = no opinion
        rsi = self.get_RSI_signal() 
        stoch = self.get_stoch_signal() 
        #this list is going to look at the values in the list and decide to buy sell or if it is trading sideways
        signal = None #this will either be buy or sell
        #code below will be added to once there is a way to add a bias calculation
        #bias will be passed in as a string of either "trending" or "ranging"
        # if bias.equals("Trending"):
        #     stoch
        # elif bias.equals("Ranging"):
        #     bias_value =
            
        if (rsi + stoch) >= 1:
            signal = "Buy"
        elif (rsi + stoch) <= -1:
            signal = "Sell"
        else: 
            signal = None
            
        return signal          
    

    def get_RSI_signal(self):
        #this method will get the rsi from the week leading up to the day it is
        rsi_object = RelativeStrength(self.ticker, self.today, self.period, self.window)
        rsi_list = rsi_object.find_rsi_range()
        previous = 0
        slope = 0
        
        if any(x <= 30.0 for x in rsi_list):
            #this looks for a value in the list, if it is 30.0 or less, then it returns true
            for i in range(len(rsi_list)):
                if rsi_list[i] >= previous:
                    slope += 1
                else:
                    slope -=1
        
        elif any(x >= 70.0 for x in rsi_list):
            #this looks for a value in the list, if it is 70.0 or more, then it returns true
            for i in range(len(rsi_list)):
                if rsi_list[i] > previous:
                    slope += 1
                else:
                    slope -=1
                           
        if slope >= 1:
            opinion = 1
        elif slope <= -1:
            opinion = -1
            
        if all(30.0 < x < 70.0 for x in rsi_list):
            #this means every value in the list is within the safe range being 30-70, meaning there is no signal to buy
            opinion = 0
           
        return opinion

    def get_stoch_signal(self):
        #this method will find the Stochastic Oscillator from the week leading up to the day it is
        stoch_object = Stochastic(self.ticker, self.today, self.period, self.window)
        stoch_list = stoch_object.stoch_list()
        
        previous = 0
        slope = 0
        
        if any(x <= 20.0 for x in stoch_list):
            for i in range(len(stoch_list)):
                if stoch_list[i] >= previous:
                    slope += 1
                else:
                    slope -=1
        
        elif any(x >= 80.0 for x in stoch_list):
            for i in range(len(stoch_list)):
                if stoch_list[i] > previous:
                    slope += 1
                else:
                    slope -=1
                           
        if slope >= 1:
            opinion = 1
        elif slope <= -1:
            opinion = -1
            
        if all(20.0 < x < 80.0 for x in stoch_list):
            #this means every value in the list is within the safe range being 20-80, meaning there is no signal to buy
            opinion = 0
        
        return opinion