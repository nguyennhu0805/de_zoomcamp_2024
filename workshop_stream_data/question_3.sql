-- Q3: answer 2

with tmp AS 
(
SELECT max (tpep_pickup_datetime) AS lastest_pickup
FROM trip_data
)

SELECT taxi_zone.Zone as pickup_zone, count (1) AS number_of_trips
FROM trip_data
JOIN taxi_zone ON trip_data.PULocationID = taxi_zone.location_id
WHERE tpep_pickup_datetime >= (SELECT lastest_pickup FROM tmp) - INTERVAL '17 hour'
GROUP BY 1
ORDER BY 2 DESC 
LIMIT 3;
