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
        self.beta
        self.ticker = yf.Ticker(ticker_name)
        self.date = start_date
        #flat value for the expected required return because all other ways of calculating seem illogical and this is ultimately up to the user
        #idea for a feature could be asking the user what kind of return they are expecting in the final product 
        self.return_with_risk = .08
        self.risk_free_rate

    #calculates expected dividend per share based on the current dividend payout and growth rate calculated in other methods and sets value to instance variable
    def EEDPS(self):
        pass

    #calculates the cost of capital equity using the CAPM model and sets value to instance variable
    def CCE(self, ticker, starting_date):
        company = DDM(ticker, starting_date)
        company.set_beta()
        company.set_year_and_date()
        company.set_risk_free_rate()
        market_risk_premium = self.return_with_risk - self.risk_free_rate
        self.cost_of_equity = self.risk_free_rate + self.beta * market_risk_premium

    #calculates the dividend growth rate using historical data from yFinance and sets value to instance variable
    def DGR(self):
        pass

    
    """
    Value is needed for the cost of equity calculations
    sets the beta for the company we are interested in using yfinance. Only issue is that the beta value is only for current day. This is a placeholder for now until I can figure out how to 
    calculate beta myself
    code for beta info gotten from: https://quant.stackexchange.com/questions/15797/how-does-yahoo-finance-calculate-beta
    """
    def set_beta(self):
        info = self.ticker.info
        self.beta = info.get('beta')

    def set_risk_free_rate(self):
        #creates list with all of the 3 month treasury bill rates by month with each value in the list being a tuple
        #first element in tuple is the date in the format YEAR-MM-DD with all dates in numbers and each value separated by a -
        #second element is a string that contains the interest rate for that month and yeear
        data = []
        # Open the CSV file in read mode
        with open('TB3MS.csv', 'r') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            # Iterate over each row in the CSV file
            for row in csv_reader:
                data.append(row)
        #first item in list is documentation on format of data, need to delete to process and can prob optimize later 
        data.pop(0)

        #another place to optimize, this is just searching for correct T bill rate based on month and year on linear search, can change to binary or something 
        for pair in data:
            #again set year month and day variables based on the delimiter '-' for row
            year, month, day = pair[0].split('-')
            #if year and month for current row matches the start date year and month then set risk free limit  
            if year == self.date[0] and month == self.date[1]:
                self.risk_free_rate = float(pair[1])
                return
            


    #string processing to override self.date with a tuple containing the year as first element and day as second, just some string processing, assuming that date was passed as the format
    #YEAR-MONTH-DAY
    def set_year_and_date(self):
        #split the string into variables of year month and day by delimiter '-'
        year, month, day = self.date.split('-')
        self.date = (year, month)

