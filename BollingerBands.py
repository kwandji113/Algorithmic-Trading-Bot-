import pandas as pd
import yfinance as yf

#ticker ="AAPL"
#data = yf.download(ticker, start ="2020-01-01", end = "2024-03-19")
#print(data.head())


def bollinger_bands(data, window, std):
  """
  This function calculates Bollinger Bands based on closing prices.

  Args:
      data (pandas.DataFrame): DataFrame containing OHLC (Open, High, Low, Close) data.
      window (int): The window size for the moving average.
      std (float): The number of standard deviations for the upper and lower bands.

  Returns:
      pandas.DataFrame: DataFrame with additional columns for Upper Band, Middle Band, and Lower Band, along with Width for volitability calculations.
  """
  rolling_mean = data['Close'].rolling(window=window).mean()
  std_dev = data['Close'].rolling(window=window).std()
  upper_band = rolling_mean + (std * std_dev)
  lower_band = rolling_mean - (std * std_dev)
  data['Upper Band'] = upper_band
  data['Middle Band'] = rolling_mean
  data['Lower Band'] = lower_band
  width = (upper_band-lower_band)/rolling_mean
  data['Width'] = width
  return data


# Download historical price data
ticker = "AAPL"
data = yf.download(ticker)

# Calculate Bollinger Bands with a 20-day window and 2 standard deviations
data = bollinger_bands(data.copy(), window=20, std=2)

# Print the data to view the added Bollinger Band columns
print(data.tail())  # View the last few rows with Bollinger Band data
