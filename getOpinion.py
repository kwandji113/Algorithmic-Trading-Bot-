import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import RelativeStrength
import Stochastic
import MovingAverages
import MACD_indicator

#this program is going to take Technical Analysis algorythms and create an opinion purely based on the numbers they return
#example: RSI safe values range from 30-70. If the number returned is 30, then goes up, it is a buy signal

class GetOpinion():
    
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.today = datetime.today().strftime('%Y-%m-%d') #returns todays date
        self.today_object = datetime.strptime(self.today, '%Y-%m-%d')
        self.period = 14
        self.window = 7 #for the week before
        

    def form_opinion(self, bias):
        #1 = buy, -1 = sell, 0 = no opinion
        rsi = self.get_RSI_signal() 
        stoch = self.get_stoch_signal() 
        ma = self.getMA()
        #this list is going to look at the values in the list and decide to buy sell or if it is trading sideways
        signal = None #this will either be buy or sell
        #code below will be added to once there is a way to add a bias calculation
        #bias will be passed in as a string of either "trending" or "ranging"
        if bias.equals("Trending"):
            #stoch will be valuable, but less so since it is more useful in a ranging market, hence it will be less value in the final calc
            stoch *= 0.5
        elif bias.equals("Ranging"):
            #rsi value will be less since stoch is a little more valuable in a ranging market
            rsi *= 0.5
        
            
        if ((rsi + stoch) * ma) >= 1:
            signal = "Buy"
        elif ((rsi + stoch) * ma) <= -1:
            signal = "Sell"
        else: 
            signal = "Hold"

            
        return signal          
    

    def get_RSI_signal(self):
        #this method will get the rsi from the week leading up to the day it is
        rsi_object = RelativeStrength.RelativeStrength(self.ticker, self.today, self.period, self.window)
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
                previous = rsi_list[i]
        
        elif any(x >= 70.0 for x in rsi_list):
            #this looks for a value in the list, if it is 70.0 or more, then it returns true
            for i in range(len(rsi_list)):
                if rsi_list[i] > previous:
                    slope += 1
                else:
                    slope -=1
                previous = rsi_list[i]
                           
        if slope >= 1:
            #opinion = 1
            opinion = slope
        elif slope <= -1:
            #opinion = -1
            opinion = slope
        #code is commented out incase my idea does not work for bias calculation

            
        if all(30.0 < x < 70.0 for x in rsi_list):
            #this means every value in the list is within the safe range being 30-70, meaning there is no signal to buy
            opinion = 0
           
        return opinion

    def get_stoch_signal(self):
        #this method will find the Stochastic Oscillator from the week leading up to the day it is
        stoch_object = Stochastic.Stochastic(self.ticker, self.today, self.period, self.window)
        stoch_list = stoch_object.stoch_list()
        
        previous = 0
        slope = 0
        
        if any(x <= 20.0 for x in stoch_list):
            for i in range(len(stoch_list)):
                if stoch_list[i] >= previous:
                    slope += 1
                else:
                    slope -=1
                previous = stoch_list[i]
        
        elif any(x >= 80.0 for x in stoch_list):
            for i in range(len(stoch_list)):
                if stoch_list[i] > previous:
                    slope += 1
                else:
                    slope -=1
                previous = stoch_list[i]
                           
        if slope >= 1:
            #opinion = 1
            opinion = slope
        elif slope <= -1:
            #opinion = -1
            opinion = slope
        #code is commented out incase my idea does not work for bias calculation
            
        if all(20.0 < x < 80.0 for x in stoch_list):
            #this means every value in the list is within the safe range being 20-80, meaning there is no signal to buy
            opinion = 0
        
        return opinion
    
    def getMACD(self):
        pass

    def getMA(self):
        num_subtract = 0
        num_days = 0
        while num_days != 30:
            current_day = self.today_object - timedelta(days = num_subtract)
            day_name = current_day.strftime("%A")
            
            if day_name == 'Saturday' or day_name == 'Sunday':
                num_subtract += 1
            else: 
                num_days += 1
                num_subtract += 1
               
        new_start_date = self.today_object - timedelta(days = num_subtract)
        ma_object = MovingAverages.MovingAverages(self.ticker)
        ma = ma_object.calculate_moving_average(50, new_start_date.strftime('%Y-%m-%d'), self.today)
        #this algorithm is going to basically find the slope of the dataspread of values returned. anything >0 up, <0 down
        #movement is going to be a SECANT line of 10n days, since 30 days is too many to get an accurate direction
        movement = (ma['Close'][len(ma) - 1] - ma['Close'][len(ma) - 11]) / 10
        # - 11 because len -1 and then the additional 10
        return movement


#testing:   
# opinion = GetOpinion('NVDA')
# rsi = opinion.get_RSI_signal()
# print(rsi)