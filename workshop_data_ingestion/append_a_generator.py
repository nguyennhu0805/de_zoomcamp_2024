import dlt
import duckdb

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

data_1 = people_1()

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

data_2 = people_2()

# define the connection to load to. 
# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(pipeline_name="customer",
						destination='duckdb', 
						dataset_name='customer_info')

# run the pipeline with default settings, and capture the outcome
info = pipeline.run(data_1, 
                    table_name="demographic", 
                    write_disposition="replace")
info = pipeline.run(data_2, 
                    table_name="demographic", 
                    write_disposition="append")

# show the outcome
conn = duckdb.connect (f'{pipeline.pipeline_name}.duckdb')
query = conn.sql ("SELECT sum (age) FROM customer_info.demographic")
print(info)
display (query)

