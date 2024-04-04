import csv
data = []
# Open the CSV file in read mode
with open('TB3MS.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        data.append(row)
print(data[1])