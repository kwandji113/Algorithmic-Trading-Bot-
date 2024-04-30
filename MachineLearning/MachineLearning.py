import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from sklearn.preprocessing import MinMaxScaler
import random
pd.set_option('display.max_columns', None)

data = yf.download(tickers = 'AAPL', start = '2012-01-01',end = '2023-01-01')

#getting our inputs, the technical indicators and all that stuff, can add more if you want
data['RSI'] = ta.rsi(data.Close, 14)
data['MACD'] = ta.macd(data.Close)
data['MA_50'] = ta.sma(data.Close, 50)
data['MA_200'] = ta.sma(data.Close, 200)
data['OBV'] = ta.obv(data.Close, data.Volume)

data['TargetNextClose'] = data['Adj Close'].shift(-1) #this is the thing the AI is trying to predict, the next days close price

data.dropna(inplace=True) #getting rid of all the NULLS/NONE

#cleaning up data
data.reset_index(inplace = True) 
data.drop(['Volume', 'Close', 'Date'], axis=1, inplace=True)

#scale data between 0 and 1 to prevent big ass numbers from providing too much weight and small numbers not providing enough
sc = MinMaxScaler(feature_range=(0,1))
data_set_scaled = sc.fit_transform(data)

X = []
backcandles = 25 #the amount of candles we are using to predict prices
n_values = 1 #this is the amount of future values you want to predict

for i in range(8): #8 is the amount of columns we are using as training data
    X.append([])
    #create the sliding window
    for j in range(backcandles, data_set_scaled.shape[0] - n_values + 1):
        X[i].append(data_set_scaled[j-backcandles:j,i]) #goes from starting index i, to i-backcandle back, and add all values of the current column

#move axis from 0 to position 2
X = np.moveaxis(X, [0], [2])
X = np.array(X)

Y = []
for i in range(backcandles - 1, data_set_scaled.shape[0] - n_values + 1): #we have backcandles -1 since we already shifted all target closing price values down
    Y.append(data_set_scaled[i:i+n_values, -1]) #grabbing current -> current + n_values which is what we want

Y = np.reshape(Y, (len(Y), n_values))


#splitting training data
#idt TF has an option to do a 3 way split like Mr. Puri told us in class
splitlimit = int(len(X)*0.8)
X_train, X_test = X[:splitlimit], X[splitlimit:]
y_train, y_test = Y[:splitlimit], Y[splitlimit:]


from keras.layers import LSTM
from keras.layers import Dense
import tensorflow as tf
from keras import optimizers
from keras.models import Model
from keras.layers import Dense, LSTM, Input, Activation, concatenate


lstm_input = Input(shape=(backcandles, 8), name='lstm_input')
inputs = LSTM(20, name='first_layer')(lstm_input)
inputs = Dense(1, name='dense_layer')(inputs)
output = Activation('relu', name='output')(inputs)
model = Model(inputs=lstm_input, outputs=output)
adam = optimizers.Adam()
model.compile(optimizer=adam, loss='mse')
model.fit(x=X_train, y=y_train, batch_size=15, epochs=5, shuffle=True, validation_split = 0.1)

y_pred = model.predict(X_test)
print(y_pred.shape)


plt.figure(figsize=(16,8))
plt.plot(y_test, color = 'black', label = 'Test')
plt.plot(y_pred, color = 'green', label = 'pred')
plt.legend()
plt.show()
