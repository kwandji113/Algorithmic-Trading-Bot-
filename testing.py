import csv
from collections import deque
import yfinance as yf
from queue import Queue
from copy import deepcopy
from typing import Deque, Generic, Tuple, TypeVar
T = TypeVar("T")
class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue:Deque = deque()

    def enqueue(self, item)->None:
        self.queue.append(item)

    def dequeue(self)->T:
        return self.queue.popleft()

    def peek(self)->T:
        if len(self.queue)>0:
            return self.queue[0]
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.queue) == 0
    def length(self) -> int:
        return len(self.queue)


msft = yf.Ticker("MSFT")
nvda = yf.Ticker("NVDA")



msft_dividends = msft.dividends
# for index, row in msft_dividends():
#     print(row['c1'], row['c2'])
print(type(msft))
print(type(msft.dividends))
print(msft.dividends[:5])
print(len(msft.dividends))


dividends = msft.dividends

# Print the DataFrame
print(dividends)

# Accessing individual elements in the DataFrame
# For example, accessing the first dividend amount and date
first_dividend_amount = dividends.iloc[0]
print(type(first_dividend_amount))
first_dividend_date = dividends.index[0]
print(type(first_dividend_date))

print("First Dividend Amount:", first_dividend_amount)
print("First Dividend Date:", first_dividend_date)
year = first_dividend_date.year
print("This was the year", year)
print("This is the type of the year " + str(type(year)))
month = first_dividend_date.month
print("This is the type of the month " + str(type(month)))
info = msft.info
beta = info.get('beta')
print(beta)
ninfo = nvda.info
betan = ninfo.get('beta')
print(type(betan))


import pandas as pd

# Assuming you have a target year and month
target_year = 2023
target_month = 5

# Calculate the target date based on the year and month
target_date = pd.Timestamp(year=target_year, month=target_month, day=1)

# Initialize variables to store the closest dividend date and the difference in days
closest_dividend_date = None
closest_difference = float('inf')  # Initialize with positive infinity

# Loop through each dividend date
for dividend_date in dividends.index:
    dividend_date = dividend_date.tz_localize(None)  # Make dividend_date timezone-naive
    target_date = target_date.tz_localize(None) 
    # Calculate the absolute difference in days between the dividend date and the target date
    difference = abs((dividend_date - target_date).days)
    
    # Check if this difference is smaller than the current closest difference
    if difference < closest_difference:
        closest_difference = difference
        closest_dividend_date = dividend_date

# Print the closest dividend date
print("Closest Dividend Date:", closest_dividend_date)

# trying to write something that will first populate a queue with the first 5 values will change to 4 
# then change it to be something that enqueues and dequeues to keep running log of yearly dividend which will then be used to calculate DGR
q = Queue()
thing = []
for x in range (20):
    thing.append(x)
counter = 0
while q.length() < 5:
    q.enqueue(thing[counter])
    counter += 1
    continue

while not q.is_empty():
    print(q.dequeue())


