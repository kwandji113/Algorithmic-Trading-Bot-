import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from sklearn.preprocessing import MinMaxScaler
#globals
TOTAL_FEATURES = 8
BACK_CANDLES = 25
FUTURE_DAYS = 1

def create_stock_dictionary():
    dictionary = {}
    current_directory = os.getcwd()
    folder_name = 'S&P500'
    folder_path = os.path.join(current_directory, folder_name)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            name = file_name.split("_")[0]
            file_path = os.path.join(folder_path, file_name)
            dictionary[name] = pd.read_csv(file_path)
            
    return dictionary

stock_data = create_stock_dictionary()
n_days = BACK_CANDLES
m_days = FUTURE_DAYS

input_seqs = []
output_seqs = []

scaler = MinMaxScaler()
#add features in here
for stock in stock_data:
    stock_data[stock].drop(['Datetime'], axis=1, inplace=True)
    stock_data[stock][stock_data[stock].columns] = scaler.fit_transform(stock_data[stock])


# [1, 2, 3, 4, 5, 6, 7],
# [12, 23, 42, 23, 34, 10, 72]
# [10, 20, 23, 91, 15, 49, 37]


# (1, 2, 3, 4)
# (12, 23, 42, 23)
# (10, 20, 23, 91)


# (2, 3, 4, 5)
# (23, 42, 23, 34)
# (20, 23, 91, 150)

        
for stock, df in stock_data.items():
    for i in range(len(df) - n_days - m_days + 1):
        input_seq = df.iloc[i:i+n_days].values
        output_seq = df.iloc[i+n_days:i+n_days+m_days]['Close'].values  
        input_seqs.append(input_seq)
        output_seqs.append(output_seq)

input_seqs = np.array(input_seqs)
output_seqs = np.array(output_seqs)
