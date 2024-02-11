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

SELECT distinct (pu_location_id)
FROM `nyc_taxi.green_taxi_partition`
WHERE DATE(TIMESTAMP_MICROS(lpep_pickup_datetime)) between '2022-06-01' and '2022-06-30'

