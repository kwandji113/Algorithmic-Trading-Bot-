import pandas as pd
import yfinance as yf
import pandas as pd

def calculate_uo(ticker, period_short=7, period_long=28, period_atr=14):
  """
  This function downloads OHLC data for a given ticker symbol and calculates the Ultimate Oscillator (UO).

  Args:
      ticker (str): The ticker symbol of the stock.
      period_short (int, optional): The period for the short-term price range. Defaults to 7.
      period_long (int, optional): The period for the long-term price range. Defaults to 28.
      period_atr (int, optional): The period for calculating the Average True Range (ATR). Defaults to 14.

  Returns:
      pandas.DataFrame: A DataFrame containing the OHLC data and the UO values.
  """
  # Download OHLC data, create empty columns for use
  data = yf.download(ticker)
  data['TR'] = pd.DataFrame(columns=['TR'])

  # Calculate UO using the previous function (modified for DataFrame input)
  high_prev_close_diff = data['High'] - data['Close'].shift(1)
  low_prev_close_diff = data['Close'].shift(1) - data['Low']
  data['TR'] = high_prev_close_diff.abs().combine_first(low_prev_close_diff.abs())


  atr = data['TR'].ewm(alpha=1/period_atr, min_periods=period_atr).mean()
  #exponential weighting moving average from the pandas library at the highest smoothening rate calculates average true range
  #high alpha is more volatiable, low alpha gets a smoother ATR focusing on older TR values
  data['Short_Range'] = data['High'].rolling(window=period_short).max() - data['Low'].rolling(window=period_short).min()
  data['Long_Range'] = data['High'].rolling(window=period_long).max() - data['Low'].rolling(window=period_long).min()
  #This mess essentially grabs the price range over the shorter range (defaulted to 7 days) and the longer range (28 days)
  atr_norm = atr / atr.max()
  short_range_norm = data['Short_Range'] / data['Short_Range'].max()
  long_range_norm = data['Long_Range'] / data['Long_Range'].max()
  #attempting to scale it down to 0 and 1 by dividing everything by its respective max (Scalar is wonky)
  uo = (4 * short_range_norm) + (3 * atr_norm) + (3 * long_range_norm)
  uo = 100 * uo / 10
  data["UO"] = uo
  #4 3 3 are the normal weights for UO, they can be adjusted
  #UO should now be scaled on 0-100, and 

  # Return DataFrame with OHLC and UO
  return data


data_with_uo = calculate_uo("AAPL")

print(data_with_uo.tail())  # Print the last few rows including UO values
