import yfinance as yf
import pandas as pd

msft = yf.Ticker("MSFT")
msft_dividends = msft.dividends
dividends_filtered = msft_dividends[(msft_dividends.index.year >= 2018) & (msft_dividends.index.year != 2024)]
# for i in range (len(msft_dividends)):
#     print("This was the date of the dividend: " + str(msft_dividends.index[i]))
#     print("This was how much the dividend was: " +str(msft_dividends.iloc[i]))
#     print(msft_dividends.index[i].month)
# for date, dividend in msft_dividends.items():
#     print("This was the date of the dividend: " + str(date))
#     print("This was how much the dividend was: " + str(dividend))
#     print(type(date))
#     print(type(dividend))
frequency = dividends_filtered.resample('Y').count()
print(frequency)
avg = round(frequency.mean())
print(f"The average number of dividend payments per year for MSFT is: {avg}")