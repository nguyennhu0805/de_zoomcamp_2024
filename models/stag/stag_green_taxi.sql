{{config(miterialized = 'view')}}

SELECT *
, {{the_macro_test_name ('total_amount')}} AS test_macro
, {{dbt_utils.surrogate_key(['vendor_id', 'lpep_pickup_datetime'])}} AS trip_id
FROM {{source ('staging', 'green_taxi')}}

{%if var('is_test_run', default = true)%}
LIMIT 10
{%endif%}