import yfinance as yf
import pandas as pd
import scipy.stats as stats
# msft = yf.Ticker("MSFT")
# msft_dividends = msft.dividends
# dividends_filtered = msft_dividends[(msft_dividends.index.year >= 2018) & (msft_dividends.index.year != 2024)]
# for i in range (len(msft_dividends)):
#     print("This was the date of the dividend: " + str(msft_dividends.index[i]))
#     print("This was how much the dividend was: " +str(msft_dividends.iloc[i]))
#     print(msft_dividends.index[i].month)
# for date, dividend in msft_dividends.items():
#     print("This was the date of the dividend: " + str(date))
#     print("This was how much the dividend was: " + str(dividend))
#     print(type(date))
#     print(type(dividend))
# frequency = dividends_filtered.resample('Y').count()
# print(frequency)
# avg = round(frequency.mean())
# print(f"The average number of dividend payments per year for MSFT is: {avg}")
# Example data
list1 = [10, 12, 14, 16, 18]
list2 = [8, 9, 10, 11, 12]

# Perform a one-sided two-sample t-test
t_stat, p_value = stats.ttest_ind(list1, list2, alternative='greater')

print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

# Interpret the p-value
alpha = 0.05  # significance level
if p_value < alpha:
    print("Reject the null hypothesis: The mean of list1 is greater than the mean of list2.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to say the mean of list1 is greater than the mean of list2.")