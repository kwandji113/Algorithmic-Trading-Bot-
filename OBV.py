import yfinance as yf
import pandas as pd
import TrendDetection
# Function to calculate the On-Balance Volume (OBV)
def calculate_obv(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['OBV'] = 0
    for i in range(1, len(data)):
        if data['Close'][i] > data['Close'][i-1]:
            data['OBV'][i] = data['OBV'][i-1] + data['Volume'][i]
        elif data['Close'][i] < data['Close'][i-1]:
            data['OBV'][i] = data['OBV'][i-1] - data['Volume'][i]
        else: 
            data['OBV'][i] = data['OBV'][i-1]
    data['CLOSE_TREND'] = TrendDetection.detectTrend(data['Close'])
    data['OBV_TREND'] = TrendDetection.detectTrend(data['OBV'])
    
    return data

ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-01-30'
obv_data = calculate_obv(ticker, start_date, end_date)
print(obv_data[['Close','CLOSE_TREND', 'OBV', 'OBV_TREND']])