import numpy as np
import pandas as pd
from scipy import stats

#lists that will store the daily returns for the NN and random 
estimated_returns = []
random_returns = []

#loop through to get predictions for all companys in S&P 500 on a given day and see which has the highest predicted growth
#return that ticker for that day 
def get_prediction(day):
    pass

#get a random stock in the S&P on a given day and calculate amount of money made or lost if bought at market open and sold at market close
#needs to be called 100 times to build data set 
def get_random_stock(day):
    #have to number off all of the stocks in the folder and generate a random number 
    #then read the csv data for a given ticker and look for the open and close date on a given date 
    #we're not buying a defined numebr of shares because that could lead to inconsistent $ amounts invested per day
    #just pretend that you can buy fractions of shares and invest $1000 daily and apply the percent change to get amount made and lost for a day
    #big idea **check to make sure that the random company you pull data for is for the market day that you are testing
    #there's the possibility that the company is delisted and does not have data for the day that you want
    pass

#calculates a 2 sided 2 sample t test and stores test statistic and p-value 
t_stat, p_value = stats.ttest_ind(estimated_returns, random_returns)
print("t_stat: " + str(t_stat))
print("pval: " + str(p_value))
if t_stat > 0:
    p_value = p_value / 2
else:
    p_value = 1 - p_value/2



