import math
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
    
def calculate_moving_average(stock_symbol, n_days, start_date, end_date) -> pd.DataFrame:
    adjusted_start_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=n_days * 1.5)).strftime('%Y-%m-%d') #add a buffer since the stock market isn't open everyday
    historical_data = yf.download(stock_symbol, adjusted_start_date, end_date)
    #get the data from start date to end date, to get the indexes
    if historical_data.empty:
        return None

    moving_averages = historical_data['Close'].rolling(window=n_days).mean().to_frame()
    aligned_moving_averages = moving_averages.loc[start_date:]

    return aligned_moving_averages

def calculate_moving_average_single_day(stock_symbol, n_days, date):
    end_date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=10)).strftime('%Y-%m-%d') #add a buffer since the stock market isn't open everyday
    return calculate_moving_average(stock_symbol, n_days, date, end_date)['Close'].iloc[0]
        
#calculate crosses, and divergence/convergence between two moving averages
def sgn(n):
    if(n > 0):
        return 1
    if(n < 0):
        return -1
    return 0

def movingAverageCross(moving_average1: pd.DataFrame, moving_average2: pd.DataFrame) -> pd.DataFrame:
    aligned_data = pd.merge(moving_average1, moving_average2, left_index=True, right_index=True, how='inner', suffixes=('_1', '_2'))
    aligned_data['difference'] = aligned_data['Close_1'] - aligned_data['Close_2']
    prev_difference = 0
    convergence_list = []
    divergence_list = []
    cross_list = []
    for i in range(len(aligned_data)):
        if(i == 0):
            convergence_list.append(False)
            divergence_list.append(False)
            cross_list.append(False)
            prev_difference = aligned_data['difference'][i]
        else:
            convergence_list.append(math.fabs(aligned_data['difference'][i]) <= math.fabs(prev_difference))
            divergence_list.append(math.fabs(aligned_data['difference'][i]) >= math.fabs(prev_difference))
            cross_list.append(sgn(prev_difference) == -1 * sgn(aligned_data['difference'][i]))
            prev_difference = aligned_data['difference'][i]
    aligned_data['Convergence'] = convergence_list
    aligned_data['Divergence'] = divergence_list
    aligned_data['Cross'] = cross_list
    return aligned_data

moving_average = calculate_moving_average('AAPL', 20, '2023-01-06', '2023-03-04')
moving_average2 = calculate_moving_average('AAPL', 200, '2024-01-01', '2024-03-04')
print(moving_average2)
