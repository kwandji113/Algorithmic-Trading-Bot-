import math
import pandas as pd
import yfinance as yf
import datetime
    
def calculate_moving_average(stock_symbol, n_days, start_date, end_date) -> pd.DataFrame:
    data = yf.Ticker(stock_symbol) #get the stock data
    historical_data = data.history(start=start_date, end=end_date) #get the data from start date to end date, to get the indexes
    if historical_data.empty:
        return None

    starting_row_name = historical_data.iloc[0].name
    ending_row_name = historical_data.iloc[-1].name

    full_data = data.history(period="max")
    
    starting_index = full_data.index.get_loc(starting_row_name) - (n_days - 1) #find our desired position in the max dataframe
    ending_index = full_data.index.get_loc(ending_row_name) #find our end_date in the max dataframe

    if starting_index < 0: #prevent out of bound errors
        return None
    relevant_data = full_data.iloc[starting_index:ending_index + 1]
    moving_averages = relevant_data['Close'].rolling(window=n_days).mean().to_frame()
    aligned_moving_averages = moving_averages.loc[starting_row_name:ending_row_name]

    return aligned_moving_averages
        
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
moving_average2 = calculate_moving_average('AAPL', 50, '2023-01-01', '2023-03-04')
print(moving_average)
