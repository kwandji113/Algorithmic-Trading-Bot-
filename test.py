import numpy as np

data_set_scaled = []
amount_of_rows = 10
amount_of_columns = 10
number = 0
for i in range(0, amount_of_rows):
    data_set_scaled.append([])
    for j in range(0, amount_of_columns):
        number += 1
        data_set_scaled[i].append(number)
data_set_scaled = np.array(data_set_scaled)
print(data_set_scaled)
n_values = 5 #this is the amount of future values you want to predict
Y = []
for i in range(0, data_set_scaled.shape[0] - n_values + 1):
    Y.append(data_set_scaled[i:i+n_values, -1]) #grabbing current -> current + n_values which is what we want
    
X = []
backcandles = 5 #the amount of previous days we are using to predict future data
for i in range(8): #8 is the amount of columns we are using as training data
    X.append([])
    #create the sliding window
    for j in range(backcandles, data_set_scaled.shape[0]):
        X[i].append(data_set_scaled[j-backcandles:j,i]) #goes from starting index i, to i-backcandle back, and add all values of the current column

print(Y)

    
    