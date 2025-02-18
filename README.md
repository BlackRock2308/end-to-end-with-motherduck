# DuckDB Data Pipeline with Dagster, dbt, and Streamlit

This repository demonstrates an end-to-end data pipeline that:
- **Ingests** data from a local PostgreSQL instance running in Docker.
- **Transforms** the data using dbt.
- **Orchestrates** the pipeline with Dagster.
- **Visualizes** the transformed data using a Streamlit dashboard.
- **Simulates** new data by inserting 10 rows into PostgreSQL every 10 minutes.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [PostgreSQL Docker Setup](#postgresql-docker-setup)
  - [Python Virtual Environment](#python-virtual-environment)
  - [MotherDuck Setup](#motherduck-setup)
  - [dbt Setup](#dbt-setup)
  - [Dagster Setup](#dagster-setup)
  - [Streamlit Setup](#streamlit-setup)
- [Usage](#usage)
  - [Simulating Data Inserts](#simulating-data-inserts)
  - [Data Ingestion](#data-ingestion)
  - [Data Transformation](#data-transformation)
  - [Orchestrating with Dagster](#orchestrating-with-dagster)
  - [Launching the Streamlit Dashboard](#launching-the-streamlit-dashboard)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project builds a modern data pipeline that ingests data from a Dockerized PostgreSQL database, loads it into MotherDuck (DuckDB as SaaS), transforms it with dbt, orchestrates tasks with Dagster, and visualizes results using Streamlit. A simulation script periodically inserts new rows (10 every 10 minutes) into PostgreSQL, demonstrating how the pipeline handles incremental data.

## Features

- **Dockerized PostgreSQL**: Local data source simulation.
- **Data Ingestion**: Python script extracts data from PostgreSQL and loads it into MotherDuck.
- **Data Transformation**: dbt transforms raw data into a structured format.
- **Orchestration**: Dagster manages and schedules pipeline tasks.
- **Visualization**: Streamlit dashboard displays transformed data interactively.
- **Data Simulation**: Script to insert 10 new rows every 10 minutes.

## Architecture

```mermaid
flowchart TD
    A[Dockerized PostgreSQL<br/>(Data Source)] --> B[Ingestion Script]
    B --> C[MotherDuck (DuckDB SaaS)<br/>(Raw Data)]
    C --> D[dbt<br/>(Transformation)]
    D --> E[Dagster<br/>(Orchestration)]
    E --> F[Streamlit Dashboard<br/>(Visualization)]


##Prerequisites
Python 3.8+
Docker and Docker Compose
Python packages:
pandas
duckdb
psycopg2
schedule
streamlit
dagster
dbt-core (install via pip or homebrew)
A MotherDuck account with connection credentials
Setup
PostgreSQL Docker Setup
Create a docker-compose.yml file with the following content:

yaml
Copy
Edit
version: '3.8'
services:
  postgres:
    image: postgres:14
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
Start the container:

bash
Copy
Edit
docker-compose up -d
Note: Ensure that the target table (e.g., my_table) is created in your PostgreSQL database.

Python Virtual Environment
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

nginx
Copy
Edit
pandas
duckdb
psycopg2
schedule
streamlit
dagster
MotherDuck Setup
Sign up for a MotherDuck account.
Obtain your connection string (e.g., motherduck://username:password@host:port/database).
Update the connection details in your scripts (ingest_data.py, etc.).
dbt Setup
Initialize a new dbt project:

bash
Copy
Edit
dbt init my_dbt_project
Configure your profiles.yml with your MotherDuck connection details.

Create a transformation model (e.g., models/transform_my_table.sql):

sql
Copy
Edit
-- models/transform_my_table.sql
WITH base AS (
  SELECT *
  FROM raw.my_table
)
SELECT 
  timestamp,
  value,
  value * 2 AS doubled_value  -- Example transformation
FROM base;
Dagster Setup
Install Dagster if not already installed.
Create a Dagster pipeline in pipeline.py (see Usage section below for an example).
Streamlit Setup
Ensure Streamlit is installed:

bash
Copy
Edit
pip install streamlit
Usage
Simulating Data Inserts
Run the simulation script to insert 10 new rows every 10 minutes into PostgreSQL:

bash
Copy
Edit
python simulate_inserts.py
Data Ingestion
Execute the ingestion script to fetch data from PostgreSQL and load it into MotherDuck:

bash
Copy
Edit
python ingest_data.py
Data Transformation
Run dbt to transform raw data:

bash
Copy
Edit
dbt run
Orchestrating with Dagster
Run the Dagster pipeline to coordinate ingestion and transformation tasks:

bash
Copy
Edit
python pipeline.py
You can also configure Dagster's scheduling to run the job automatically.

Launching the Streamlit Dashboard
Start the Streamlit app to visualize the transformed data:

bash
Copy
Edit
streamlit run app.py
The dashboard will query and display the latest transformed data.

Project Structure
graphql
Copy
Edit
.
├── docker-compose.yml         # Docker configuration for PostgreSQL
├── simulate_inserts.py        # Script to simulate data insertion into PostgreSQL
├── ingest_data.py             # Script to ingest data from PostgreSQL to MotherDuck (DuckDB)
├── pipeline.py                # Dagster pipeline orchestration
├── app.py                     # Streamlit dashboard app
├── dbt_project/               # dbt project folder (models, profiles.yml, etc.)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
Troubleshooting
Connection Issues:
Verify that the connection strings for PostgreSQL and MotherDuck are correct.

Docker Issues:
Ensure Docker is running and the PostgreSQL container is up.

dbt Errors:
Check the profiles.yml configuration and ensure your models are correctly defined.

Dagster Issues:
Confirm Dagster is installed and your pipeline is properly defined.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes. If you have any questions or need assistance, please open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.
