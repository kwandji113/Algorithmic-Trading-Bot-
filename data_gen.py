import random
import datetime

start_date_training = datetime.date(1982, 2, 1)
end_date_training = datetime.date(2006, 2, 1)

start_date_testing = datetime.date(2006, 2, 1)
end_date_testing = datetime.date(2018, 2, 1)

start_date_validation = datetime.date(2018, 2, 1)
end_date_validation = datetime.date(2022, 2, 1)

number_of_data_points = 1000000



def data_gen(start_date, end_date):
    random_dates = set()
    i = 0
    while i < number_of_data_points:
        time_delta = end_date - start_date
        random_days = random.randint(0, time_delta.days)
        random_date = start_date + datetime.timedelta(days=random_days)
        random_dates.add(str(random_date) + "/" +str(random.randint(0,499)))
        i = i + 1
    return random_dates
    
#Accounts for changes in the SP500
def get_stock_ticker(stock_index):
    pass