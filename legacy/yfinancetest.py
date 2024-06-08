import yfinance as yf
import random
import datetime

msft = yf.Ticker("WRB")



start_date_testing = datetime.date(2006, 2, 1)
end_date_testing = datetime.date(2018, 2, 1)

random_date = start_date_testing + datetime.timedelta(days=14)


print(msft.history(start = start_date_testing, end = random_date))