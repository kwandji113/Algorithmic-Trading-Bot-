#TODO figure out how i can get all of the information i need from the ticker function for yFinance and then implement 2 main methods that will return the DDM calculation with 2 diff parameters
#one that is set on a day and another that is set on a timeframe ie. one that just gives me the day and another that gives me a time over a period
#for me that will matter less because the calculation is still going to be the same, i just need to get the data based on a diff time period. 
import yfinance as yf
import pandas as pd
msft = yf.Ticker("MSFT")
#experimentation that is commented out 

# msft_dividends = msft.dividends
# for index, row in msft_dividends():
#     print(row['c1'], row['c2'])
# print(type(msft))
# print(type(msft.dividends))
# print(msft.dividends[:5])
# print(len(msft.dividends))


dividends = msft.dividends

# Print the DataFrame
print(dividends)

# Accessing individual elements in the DataFrame
# For example, accessing the first dividend amount and date
first_dividend_amount = dividends.iloc[0]
print(first_dividend_amount)
first_dividend_date = dividends.index[1]
print(type(first_dividend_date))

print("First Dividend Amount:", first_dividend_amount)
print("First Dividend Date:", first_dividend_date)

class EEDPS: 
    def __init__(self, ticker, start_date):
        self.ticker = ticker
        self.expected_dividend 
        self.cost_of_equity 
        self.dividend_growth_rate

    #calculates expected dividend per share based on the current dividend payout and growth rate calculated in other methods and sets value to instance variable
    def EEDPS(self):
        pass

    #calculates the cost of capital equity using the CAPM model and sets value to instance variable
    def CCE(self):
        pass

    #calculates the dividend growth rate using historical data from yFinance and sets value to instance variable
    def DGR(self):
        pass

