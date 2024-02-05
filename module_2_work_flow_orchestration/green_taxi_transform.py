import pandas as pd
from stringcase import snakecase

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

def camel_to_snake(camel_case):
    #break words
    for i in range (len (camel_case)-1):
        if ( (camel_case[i].islower() and camel_case[i+1].isupper())
        or (camel_case[i].isupper() and camel_case[i+1].isupper() and camel_case[i+2].islower())
        ):
            camel_case = camel_case[:i+1] + '_' + camel_case[i+1:] 
            i = i+1
    #lower
    snake_cases = camel_case.lower()
    return (snake_cases)

@transformer
def export_data(data, *args, **kwargs):
    # 1. Remove zero passenger count or zero trip distance
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    print (f'{len(data)} rows left after step 1')

    # 2. Insert column lpep_pickup_date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # 3. Rename columns in Camel Case to Snake Case
    n = 0
    new_col = []
    for i in data.columns:
        snake = camel_to_snake (i)
        if i != snake:
            n = n + 1
        new_col.append (snake)
    data.columns = new_col
    print (f'{n} columns are formatted to snake case')
    
    vendor = set (data['vendor_id'])
    print (f'Remain values of Vendor ID are {vendor}')
    return data


