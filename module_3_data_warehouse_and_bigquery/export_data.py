import pyarrow.parquet as pq
import pyarrow as pa
import os
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/theta-byte-412315-6ae5e5ea3f94.json'
project_id = 'theta-byte-412315'
bucket_name = 'mage-zoomcamp-matt-palmer-nn'
table_name = 'green_taxi'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data: DataFrame, **kwargs) -> None:
    # upload data to GCS bucket
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs,
        existing_data_behavior='overwrite_or_ignore'
    )
    # Specify your data exporting logic here



