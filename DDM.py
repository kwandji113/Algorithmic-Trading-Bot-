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
        self.data = yf.Ticker(ticker_name)
        self.date = start_date
        #dividend that is paid numerous times
        self.dividend
        #full dividend that is paid in the year
        self.full_dividend
        self.current_price
        

    #calculates expected dividend per share based on the current dividend payout and growth rate calculated in other methods and sets value to instance variable
    def predicted_dividend(self, symbol, starting_date):
        #set instance variables with the number of divdends paid out yearly, DGR, and current dividend payout
        data = DDM(symbol, starting_date)
        payout_frequency = data.num_dividends(symbol)
        data.DGR(symbol, starting_date)
        self.full_dividend = self.dividend * payout_frequency
        #set expected dividend
        self.expected_dividend = self.full_dividend * self.dividend_growth_rate
        

        
    def get_current_price(self, symbol, starting_date):
        stock_data = yf.download(symbol, start=starting_date, end=starting_date)
        #some code to get the price of a stock with some exception handling in case the day given is when the market is closed 
        try:
            # Fetch the historical data for the specified date range
            stock_data = yf.download(symbol, start=starting_date, end=pd.to_datetime(starting_date) + pd.Timedelta(days=1))

            # Check if data is available for the specified date
            if starting_date in stock_data.index:
                # Extract the stock price for the specified date
                price = stock_data.loc[starting_date]['Close']
                self.current_price = price
            else:
                return
        except Exception as e:
            return

    #calculates the cost of capital equity using the CAPM model: (dividends per share/current market value of stock) + dividend growth rate and sets value to instance variable
    def CCE(self, ticker, starting_date):
        company = DDM(ticker, starting_date)
        company.predicted_dividend(ticker, starting_date)
        company.get_current_price(ticker, starting_date)
        self.cost_of_equity = (self.full_dividend / self.current_price) + self.dividend_growth_rate

    #returns percent diff between what is the "true market value" and the actual market value
    def true_value (self, symbol, starting_date):
        company = DDM(symbol, starting_date)
        company.CCE(symbol, starting_date)
        predicted_value = self.expected_dividend / (self.cost_of_equity - self.dividend_growth_rate)
        percent_difference = predicted_value / self.current_price
        return percent_difference


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
        for dividend_date in company.data.dividends.index:
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
        historic_dividends = []
        closest_dividend_month = closest_dividend_date.month

        #add all dividends to a list until you hit the closest dividend date 
        #loop through using indexes in a for loop with range and check to see if the date matches with the closest dividend date, if it does then break 

        for i in range(len(company.data.dividends)):
            cur_date = company.data.dividends.index[i]
            cur_dividend = company.data.dividends.iloc[i]
            #if the month matches then add to the list
            if cur_date.month == closest_dividend_month:
                historic_dividends.append((cur_date, cur_dividend))
            
            #if the date is the closest dividend date then you can break 
            if cur_date == closest_dividend_date:
                self.dividend = cur_dividend
                break

            # #checks if list is empty if so just add in the dividend price 
            # if not historic_dividends:
            #     historic_dividends.append(cur_dividend)
            # #don't need to check the date because you're assuming that they only increase the price once a year and also in MSFT dividends dividend value could be diff in the same year
            # #just need to check if the price is different because you're assuming that price changes only occur yearly 
            # #if price is different then it's increased for the year and you can add to list 
            # elif historic_dividends[-1] != cur_dividend:
            #     historic_dividends.append(cur_dividend)
        
        #loop through to calculate avg growth rate and return 
        avg_growth = []
        historic_dividends = historic_dividends[-4]
        for i in range (len(historic_dividends) - 1):
            growth = historic_dividends[i+1]/historic_dividends[i] - 1
            avg_growth.append(growth)
        growth_rate = sum(avg_growth)/ len(avg_growth)
        #sets the dividend growth rate instance var
        self.dividend_growth_rate = growth_rate
        
    def num_dividends(self, symbol):
        #the logic is that you can't include 2024 data bc it can skew it negatively since the year isn't done so you just average the recent years to find the average number of dividends
        #a year 
        company_dividends = yf.Ticker(symbol).dividends
        filtered_dividends = company_dividends[(company_dividends.index.year >= 2018) & (company_dividends.index.year != 2024)]
        frequency = filtered_dividends.resample('Y').count()
        return frequency


    #temporarily commenting this out bc i dont think i need it 

    # #string processing to override self.date with a tuple containing the year as first element and day as second, just some string processing, assuming that date was passed as the format
    # #YEAR-MONTH-DAY
    # def set_year_and_date(self):
    #     #split the string into variables of year month and day by delimiter '-'
    #     year, month, day = self.date.split('-')
    #     self.date = (year, month)

"""
things you may need to delete 
def set_year_and_date, I think you can just use the date time objects instead of setting it as an instance variable
"""
#testing
