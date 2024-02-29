{{config(miterialized = 'view')}}

SELECT vendor_id, pu_location_id, do_location_id, trip_distance, trip_id
FROM {{ref ('stag_green_taxi')}}
UNION ALL 
SELECT vendorid, pulocationid, dolocationid, trip_distance, trip_id
FROM {{ref ('stag_yellow_taxi')}}