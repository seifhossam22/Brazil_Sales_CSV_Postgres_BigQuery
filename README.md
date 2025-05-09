# Brazil Sales Data Pipeline: CSV → Postgres → BigQuery

## Overview

This repository demonstrates a complete data engineering workflow for processing Brazilian e-commerce sales data. The pipeline covers the journey from raw CSV files, through staging and transformation in PostgreSQL, to final loading into Google BigQuery for analytics.

---

## Repository Structure

- **CreatingTablesPostgresScript/**
  - SQL scripts to create the necessary tables in PostgreSQL for storing the raw sales data.
- **Loading_script/**
  - Scripts (typically Python or Bash) to load the CSV files into the corresponding PostgreSQL tables.
- **PostgresToBigQueryUtility/**
  - Scripts and utilities to extract data from PostgreSQL and load it into Google BigQuery.

---

## Project Workflow

### 1. Prepare the PostgreSQL Database

- Use the SQL scripts in `CreatingTablesPostgresScript/` to create all required tables in your PostgreSQL instance.


### 2. Load CSV Data into PostgreSQL

- Use the scripts in `Loading_script/` to import the raw CSV files into the PostgreSQL tables you just created.



### 3. Transfer Data from PostgreSQL to BigQuery

- Use the utilities in `PostgresToBigQueryUtility/` to extract data from PostgreSQL and load it into Google BigQuery.
- This may involve exporting data to intermediate files (like CSV or Parquet) and then uploading to BigQuery, or using direct connectors.
- Example:



### 4. Data Analytics in BigQuery

- Once the data is in BigQuery, you can run SQL queries or connect BI tools for further analysis.

---

## Prerequisites

- **PostgreSQL** installed and running.
- **Google Cloud Platform** account with BigQuery enabled.
- Required Python packages:  
- `psycopg2`, `pandas`, `google-cloud-bigquery`, etc.

---

## Author

**Seif Hossam**  
[GitHub](https://github.com/seifhossam22) | [LinkedIn](https://www.linkedin.com/in/seifhossam22/)

---

## License

For educational and portfolio purposes only.

---

*Feel free to reach out for questions or collaboration!*
