import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    
    src_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green'

    taxi_dtypes = {
        'VendorID': 'Int64',
        'store_and_fwd_flag': 'str',
        'RatecodeID': 'Int64',
        'PULocationID': 'Int64',
        'DOLocationID': 'Int64',
        'passenger_count': 'Int64',
        'trip_distance': 'float64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'ehail_fee': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'payment_type': 'float64',
        'trip_type': 'float64',
        'congestion_surcharge': 'float64'
    }

    #parse_dates_green_taxi = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    parse_dates_green_taxi = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    #Input time
    year = 2020
    start_month = 10
    n = 3
    for i in range (n): #n is number of month
        month = start_month + i
        file_name = f'green_tripdata_{year}-{month}'
        url = f'{src_url}/{file_name}.csv.gz'
        df_tmp = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates_green_taxi)
        if month == start_month:
            df = df_tmp
        else:
            df = pd.concat([df, df_tmp])
        print (f'Done {file_name}')
            
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
