CREATE OR REPLACE EXTERNAL TABLE
  `theta-byte-412315.nyc_taxi.green_taxi_external`
  OPTIONS(
    format ="parquet",
    uris = ['gs://mage-zoomcamp-matt-palmer-nn/green_taxi/lpep_pickup_date=2022-*']
    );

create or replace table `theta-byte-412315.nyc_taxi.green_taxi` as
SELECT * except (__index_level_0__)
FROM `theta-byte-412315.nyc_taxi.green_taxi_external`
