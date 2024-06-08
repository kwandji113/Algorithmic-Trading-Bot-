import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
from keras import optimizers
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Dense, LSTM, Input, Activation
from tensorflow.python.keras.callbacks import EarlyStopping

class NeuralNetwork:

    def __init__(self, ticker, backcandles):
        pd.set_option('display.max_columns', None)
        self.ticker = ticker
        self.backcandles = backcandles


    #Returns array of scaled data
    def collect_data(self):
        data = yf.download(tickers=self.ticker, start='2024-06-04', interval="2m")
        MACD = ta.macd(data.Close)
        data["MACD"] = MACD["MACD_12_26_9"]
        data['RSI'] = ta.rsi(data.Close)
        data['OBV'] = ta.obv(data.Close, data.Volume)
        data['TargetNextClose'] = data['Adj Close'].shift(-1) #answer to model
        data.dropna(inplace=True)
        data.reset_index(inplace = True)
        data.drop(['Close', 'Datetime'], axis=1, inplace=True)
        sc = MinMaxScaler(feature_range=(0,1))
        data_set_scaled = sc.fit_transform(data)
        return pd.DataFrame(data_set_scaled)
    
    #always predict 1 future interval, assumes that TargetNextClose is in the last col
    def pre_process_data(self, data_set):
        x_tr, x_ts, y_tr, y_ts = [],[],[],[]
        splitindex = int(len(data_set) * .8)
        train_set, test_set = data_set[:splitindex], data_set[splitindex:]
        
        for i in range(len(train_set) - self.backcandles):
            interval_set = train_set.iloc[i:(i + self.backcandles), :-1]
            x_tr.append(train_set.iloc[i:(i + self.backcandles):, :-1])
            y_tr.append(interval_set.iloc[0,-1])
        x_ts = test_set.iloc[:, :-1]
        y_ts = test_set.iloc[:, -1]

        x_ts = np.array(x_ts)
        x_tr = np.array(x_tr)

        x_ts.reshape(x_ts.shape[0], 1, x_ts.shape[1])
        x_tr.reshape(x_tr.shape[0], 1, x_tr.shape[1])

        return [x_tr, y_tr, x_ts, y_ts]

    
    def train_model(self, x_tr, y_tr):
        model = Sequential()
        num_features = len(x_tr[0])
        #based off of robert's hyper para model
        model.add(LSTM(units= 40,activation='relu', input_shape=(self.backcandles, num_features), return_sequences=1))
        model.add(Dense(1, activation='linear'))
        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_tr, y_tr, epochs=8, batch_size=32, validation_split=0.2, callbacks=[EarlyStopping(patience=3)])
        model.save("AngusFinal.keras")  






nn = NeuralNetwork("MSFT", 40)

raw_data_set = nn.collect_data()
data_set = nn.pre_process_data(raw_data_set)

nn.train_model(data_set[0], data_set[1])


