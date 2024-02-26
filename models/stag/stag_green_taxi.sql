{{config(miterialized = 'view')}}

SELECT *, {{the_macro_test_name ('total_amount')}} AS test_macro
FROM {{source ('staging', 'green_taxi')}}
LIMIT 100