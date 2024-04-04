import csv
import yfinance as yf
data = []
# Open the CSV file in read mode
with open('TB3MS.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        data.append(row)
print(type(data[1]))

msft = yf.Ticker("MSFT")
nvda = yf.Ticker("NVDA")



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
info = msft.info
beta = info.get('beta')
print(beta)
ninfo = nvda.info
betan = ninfo.get('beta')
print(betan)
