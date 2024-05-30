import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

all_SP_stocks = []
current_directory = os.getcwd()
folder_name = 'S&P500'
folder_path = os.path.join(current_directory, folder_name)
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        name = file_name.split("_")[0]
        all_SP_stocks.append(name)


data_amount = 4000
start_date = datetime.datetime.now() - datetime.timedelta(days=data_amount)
end_date = datetime.datetime.now()
for name in all_SP_stocks:
    data = yf.download(name, start=start_date, end=end_date, interval='1d')
    data.to_csv(f'S&P500Daily/{name}_10YearDaily_stock_data.csv')


            