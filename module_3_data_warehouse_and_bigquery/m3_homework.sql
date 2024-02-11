-- Question 1:
SELECT count (1) 
FROM `theta-byte-412315.nyc_taxi.green_taxi`;


-- Question 2:
SELECT count (distinct pu_location_id) 
FROM `theta-byte-412315.nyc_taxi.green_taxi_external`;

SELECT count (distinct pu_location_id) 
FROM `theta-byte-412315.nyc_taxi.green_taxi`;


-- Question 3:
SELECT count (1) 
FROM `theta-byte-412315.nyc_taxi.green_taxi`
WHERE fare_amount = 0;


-- Question 5:
SELECT distinct (pu_location_id)
FROM `nyc_taxi.green_taxi`
WHERE DATE(TIMESTAMP_MICROS(lpep_pickup_datetime)) between '2022-06-01' and '2022-06-30'

CREATE OR REPLACE TABLE `theta-byte-412315.nyc_taxi.green_taxi_partition`
PARTITION BY lpep_pickup_date AS
SELECT *, date(timestamp_micros (lpep_pickup_datetime)) AS lpep_pickup_date
FROM `theta-byte-412315.nyc_taxi.green_taxi`;

SELECT distinct (pu_location_id)
FROM `nyc_taxi.green_taxi_partition`
WHERE lpep_pickup_date between '2022-06-01' and '2022-06-30'

