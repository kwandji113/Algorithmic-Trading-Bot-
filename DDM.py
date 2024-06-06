#TODO figure out how i can get all of the information i need from the ticker function for yFinance and then implement 2 main methods that will return the DDM calculation with 2 diff parameters
#one that is set on a day and another that is set on a timeframe ie. one that just gives me the day and another that gives me a time over a period
#for me that will matter less because the calculation is still going to be the same, i just need to get the data based on a diff time period. 
import yfinance as yf
import pandas as pd
import csv

#guideline source for all calculations: https://web.archive.org/web/20231005030422/https://www.stock-analysis-on.net/NYSE/Market-Risk-Premium
class DDM: 
    #see if you can delete some of these instance variables and just return instead
    def __init__(self, ticker_name, start_date: str):
        self.ticker_name = ticker_name
        self.expected_dividend 
        self.cost_of_equity 
        self.dividend_growth_rate
        self.ticker = yf.Ticker(ticker_name)
        self.date = start_date
        

    #calculates expected dividend per share based on the current dividend payout and growth rate calculated in other methods and sets value to instance variable
    def EEDPS(self):
        pass

    #calculates the cost of capital equity using the CAPM model: (dividends per share/current market value of stock) + dividend growth rate and sets value to instance variable
    def CCE(self, ticker, starting_date):
        company = DDM(ticker, starting_date)
        company.set_beta()
        company.set_year_and_date()
        company.set_risk_free_rate()
        market_risk_premium = self.return_with_risk - self.risk_free_rate
        self.cost_of_equity = self.risk_free_rate + self.beta * market_risk_premium

    #calculates the dividend growth rate using historical data from yFinance and sets value to instance variable
    def DGR(self, symbol, starting_date):
        #a lot of the code below is from chatGPT and hasn't been tested yet so might cause errors 

        """""
        I'm not sure if i need to make a DDM object here I don't think so but check this later 
        """
        company = DDM(symbol, starting_date)
        #loop through dividends to find dividend that matches with start year and find dividend date that is closest to the start month
        given_date = pd.Timestamp(year=self.date[0], month=self.date[1])
        given_date = given_date.tz_localize(None)
        #initialize variables to store closest difference and closest dividend date for checks in loop below
        closest_dividend_date = None
        closest_difference = float('inf')

        #might have to change this to in range for loop so that I can access the index
        for dividend_date in company.ticker.dividends.index:
            #localize method on dividend date and given date is done because they had different timezone states
            #one was naive and another was aware and because of this i couldn't calculate the difference from subtracting the TimeStamp objects
            #localize methods standardizes the TimeStamp objects so I can do work on them 
            dividend_date = dividend_date.tz_localize(None)
            #the other way of getting the day amount on a timestamp obj is ".day" not ".days" this could cause issues with syntax need to test
            difference = abs((dividend_date - given_date).days)

            #have to make sure that the closest dividend date that is set is before the given starting date
            if difference < closest_difference and dividend_date < given_date:
                closest_dividend_date = dividend_date
                closest_difference = difference
        #use a queue to enqueue and dequeue to always have a queue of the 5 most recent year's dividends 





    #string processing to override self.date with a tuple containing the year as first element and day as second, just some string processing, assuming that date was passed as the format
    #YEAR-MONTH-DAY
    def set_year_and_date(self):
        #split the string into variables of year month and day by delimiter '-'
        year, month, day = self.date.split('-')
        self.date = (year, month)

"""
things you may need to delete 
def set_year_and_date, I think you can just use the date time objects instead of setting it as an instance variable
"""
