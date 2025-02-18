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

## Architecture



Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes. If you have any questions or need assistance, please open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.
