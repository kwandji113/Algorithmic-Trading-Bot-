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
first_dividend_date = dividends.index[0]
print(type(first_dividend_date))

print("First Dividend Amount:", first_dividend_amount)
print("First Dividend Date:", first_dividend_date)