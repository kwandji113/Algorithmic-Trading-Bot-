import yfinance as yf
import pandas as pd
import numpy as np

"""
    This function calculates the Average Directional Index (ADX) for a given DataFrame 'data'
    with a specified period 'n'.

    Args:
        data (pandas.DataFrame): DataFrame containing 'High', 'Low', 'Close' price columns.
        n (int, optional): The number of periods for calculating the ADX. Defaults to 14.

    Returns:
        pandas.DataFrame: The original DataFrame with additional 'PDI', 'NDI', 'ADX' columns.
"""
def calculate_adx(data, n=14):
    
        # Calculate the True Range (TR)
        data['TR'] = np.maximum(data['High'] - data['Low'], np.maximum(data['High'] - data['Close'].shift(1), data['Close'].shift(1) - data['Low']))

        # Calculate the Up Move (UM)
        data['Up Move'] = np.where(data['High'] > data['Close'].shift(1), data['High'] - data['Close'].shift(1), 0)

        # Calculate the Down Move (DM)
        data['Down Move'] = np.where(data['Close'].shift(1) > data['Low'], data['Close'].shift(1) - data['Low'], 0)

        # Smooth the Up Move (Smoothed Up Move)
        data['Smoothed Up Move'] = data['Up Move'].ewm(alpha=1/n, min_periods=n).mean()

        # Smooth the Down Move (Smoothed Down Move)
        data['Smoothed Down Move'] = data['Down Move'].ewm(alpha=1/n, min_periods=n).mean()

        # Calculate the Positive Directional Indicator (PDI)
        data['PDI'] = 100 * data['Smoothed Up Move'] / data['TR']

        # Calculate the Negative Directional Indicator (NDI)
        data['NDI'] = 100 * data['Smoothed Down Move'] / data['TR']

        # Calculate the Directional Movement Index (DX)
        data['DX'] = np.abs(data['PDI'] - data['NDI']) / (data['PDI'] + data['NDI']) * 100  # Avoid division by zero

        # Calculate the Smoothed DX (ADX)
        data['ADX'] = data['DX'].ewm(alpha=1/n, min_periods=n+1).mean()  # Consider initial n+1 values for smoothing

        return data
    
ticker = 'AAPL'
data = yf.download("AAPL")
adx = calculate_adx(data.copy())
print(adx.tail())