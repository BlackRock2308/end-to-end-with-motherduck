# DuckDB Data Pipeline with Dagster, dbt, and Streamlit

This repository demonstrates an end-to-end data pipeline that:
- **Ingests** data from a local PostgreSQL instance running in Docker.
- **Transforms** the data using dbt.
- **Orchestrates** the pipeline with Dagster.
- **Visualizes** the transformed data using a Streamlit dashboard.
- **Simulates** new data by inserting 10 rows into PostgreSQL every 10 minutes.

## Overview

This project builds a modern data pipeline that ingests data from a Dockerized PostgreSQL database, loads it into MotherDuck (DuckDB as SaaS), transforms it with dbt, orchestrates tasks with Dagster, and visualizes results using Streamlit. A simulation script periodically inserts new rows (10 every 10 minutes) into PostgreSQL, demonstrating how the pipeline handles incremental data.

## Features

- **Dockerized PostgreSQL**: Local data source simulation.
- **Data Ingestion**: Python script extracts data from PostgreSQL and loads it into MotherDuck.
- **Data Transformation**: dbt transforms raw data into a structured format.
- **Orchestration**: Dagster manages and schedules pipeline tasks.
- **Visualization**: Streamlit dashboard displays transformed data interactively.
- **Data Simulation**: Script to insert 10 new rows every 10 minutes.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Python packages:
  - pandas
  - duckdb
  - psycopg2
  - schedule
  - streamlit
  - dagster
  - dbt-core (install via pip or homebrew)
- A MotherDuck account with connection credentials

## Setup

### PostgreSQL Docker Setup

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:latest
    container_name: postgres_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: my_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:  
```

### Populate PostgreSQL with Sample Data

```
docker cp data/fact_conso_region.csv postgres_db:/fact_conso_region.csv

```

After that you can run the following command to populate the PostgreSQL database with the sample data.

```
COPY consumption_data(annee, operateur_id, id_filiere, code_region, code_grand_secteur, pdl, conso, code_categorie_consommation, code_naf)
FROM '/fact_conso_region.csv'
DELIMITER ','
CSV HEADER;
COPY 11104 
```

postgres_db is the container name of the PostgreSQL instance.

``` 
docker-compose up -d 
```

#### Python Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### MotherDuck Setup
1. Sign up for a MotherDuck account.
2. Obtain your connection string (e.g., motherduck://username:password@host:port/database).
3. Update the connection details in your scripts (ingest_data.py, etc.).
dbt Setup

### dbt Setup

```
dbt init my_dbt_project
```