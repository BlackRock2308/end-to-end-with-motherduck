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
