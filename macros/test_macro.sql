{# This block is just the comment and will not affect how that macro work#}

{% macro the_macro_test_name (parameter) -%}

case 
when {{parameter}} = 0 then 'zero'
when {{parameter}} > 0 then '+'
when {{parameter}} <= 0 then '-'
end 

{%- endmacro%}