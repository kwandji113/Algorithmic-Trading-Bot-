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



#method to get p val and t statistic given the data sets
#predicted should be a list containing all of the changes in $ for using neural network 
#random should be a list containing all of the changes in $ for using random selection s
#returns True if null is rejected and false if it isn't 
def one_sided_2_sample_test(predicted: list, random: list) -> bool:
    # Perform a one-sided two-sample t-test to see if predictions are greater than random 
    _, p_value = stats.ttest_ind(predicted, random, alternative='greater')
    # Interpret the p-value
    alpha = 0.05  # significance level
    if p_value < alpha:
        return True
    else:
        return False
       
list1 = [10, 12, 14, 16, 18]
list2 = [8, 9, 10, 11, 12]
print(one_sided_2_sample_test(list1, list2))
"""
number off the companies taht you're selecting from 0-x 
start 100 market days before present day, for each day generate a random number that will correlate to the stock chosen, 
buy $5000 at market open and sell at market close and see the dollar change from start to end day
repeat 99 more time to get a lsit of 100 days predicted using random selection of stocks

for model predictor:
starting at 100 market days before present get predictions for each of the available companies that you're choosing from and see which one had
the greatest predcited percent gain then choose that company for the market open and close with $5k invested and store the dollar change in value
in list 
repeat 99 more times to get list of size 100 containing 100 days worth of market predictions 

perform t test using libraries with the 2 datasets and interpret value 
"""