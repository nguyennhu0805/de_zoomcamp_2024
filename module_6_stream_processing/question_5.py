import json
import time 
import pandas as pd
import gzip
from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=json_serializer
)

producer.bootstrap_connected()

t0 = time.time()

topic_name = 'test-topic'

file_path = 'green_tripdata_2019-10.csv.gz'
selected_columns = [
    'lpep_pickup_datetime',
    'lpep_dropoff_datetime',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'tip_amount'
]

with gzip.open(file_path, 'rt') as f:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(f, usecols = selected_columns)

df_green = df.head()
for row in df_green.itertuples(index=False):
    row_dict = {col: getattr(row, col) for col in row._fields}
    producer.send(topic_name, value=row_dict)

t2 = time.time()

producer.flush()

t1 = time.time()
print(f'took {(t1 - t0):.2f} seconds')
print(f'Sending took {(t2 - t0):.5f} seconds')
print(f'Flush took {(t1- t2):.5f} seconds')
