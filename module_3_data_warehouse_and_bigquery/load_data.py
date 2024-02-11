import pandas as pd
import pyarrow.parquet as pq
import io
import requests
import pyarrow as pa

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs): 
    # information
    year = 2022
    start_month = 1
    end_month = 12

    # read files
    for i in range (start_month, end_month+1):
        if i < 10:
            month = f'0{str(i)}'
        else:
            month = str (i)
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month}.parquet'

        # Get data from link
        response = requests.get(url)
        parquet_file = io.BytesIO(response.content)
        table = pq.read_table(parquet_file)
        df = table.to_pandas()
        if (i == start_month):
            data = df
        else:
            data = data.append(df)
        print (i)
        print (len (data))

    return (data)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

