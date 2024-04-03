-- Q2: answer 4
DROP MATERIALIZED VIEW trip_pairs;
CREATE MATERIALIZED VIEW trip_pairs AS
with tmp AS 
(
 SELECT taxi_zone.Zone as pickup_zone, taxi_zone_1.Zone as dropoff_zone, DATE_PART('minute', tpep_dropoff_datetime - tpep_pickup_datetime) AS trip_time
 FROM trip_data
 JOIN taxi_zone ON trip_data.PULocationID = taxi_zone.location_id
 JOIN taxi_zone as taxi_zone_1 ON trip_data.DOLocationID = taxi_zone_1.location_id
)

SELECT pickup_zone, dropoff_zone, AVG (trip_time) AS avg_trip_time, MIN (trip_time) AS min_trip_time, MAX (trip_time) AS max_trip_time, COUNT (1) AS number_of_trips
FROM tmp
GROUP BY 1, 2;
