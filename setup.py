import duckdb
import pandas as pd

# Read your raw data
df_region = pd.read_csv('data/fact_conso_region.csv')

# Replace YOUR_TOKEN with your MotherDuck API token
conn = duckdb.connect(f'md:?motherduck_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNtYmF5ZUBlcHQuc24iLCJzZXNzaW9uIjoic21iYXllLmVwdC5zbiIsInBhdCI6ImcxbURYbkpqR1VuTFc2VmlmUWxENmdLcU8ybGViaWROVDNXOUNrNEdhR1EiLCJ1c2VySWQiOiI4M2NhMzQ5My1hOTI0LTQ0OGUtODFiZi1kYjY5MzkxZDQ5NjUiLCJpc3MiOiJtZF9wYXQiLCJyZWFkT25seSI6ZmFsc2UsInRva2VuVHlwZSI6InJlYWRfd3JpdGUiLCJpYXQiOjE3Mzk4NzMyODF9.oSAk4yvkqte1OlU1uBl1KaVZs2HsvSoVo4N6rrT726Y')


# Load data into a raw table
conn.execute("CREATE SCHEMA IF NOT EXISTS bronze;")
conn.execute("DROP TABLE IF EXISTS bronze.fact_conso_region;")
conn.execute("CREATE TABLE bronze.fact_conso_region AS SELECT * FROM df_region;")

print("Data ingestion complete!")


#md:ms_electricity



# Connect to MotherDuck (using a hypothetical connection string)
#conn = duckdb.connect('motherduck://username:password@host:port/database')


