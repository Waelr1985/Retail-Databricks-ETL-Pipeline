# 🛍️ Retail Databricks ETL Pipeline

## Overview
This project demonstrates an **end-to-end ETL pipeline** using **Databricks + PySpark** on a retail dataset (Sample Superstore).  
It follows the **Medallion Architecture** (Bronze → Silver → Gold) and showcases how raw sales data can be transformed into business-ready analytics.

## Architecture
- **Bronze Layer** → Ingest raw retail sales data from CSV into Delta Lake.
- **Silver Layer** → Clean and standardize fields (dates, null handling, renaming).
- **Gold Layer** → Aggregate sales & profit by Category and Region for reporting.

## Tech Stack
- **Databricks Community Edition**
- **PySpark**
- **Delta Lake**
- **Databricks SQL / Dashboards**

## Pipeline Flow
1. **Ingestion (Bronze)** → Load `/FileStore/tables/superstore.csv` into `bronze_superstore`.
2. **Transformation (Silver)** → Clean and normalize dataset into `silver_superstore`.
3. **Aggregation (Gold)** → Build `gold_sales_summary` for BI dashboards.

## Example Analytics
- Sales by Category & Region
- Profit contribution by Category
- Regional profitability trends

## How to Run
1. Clone this repo into Databricks Repos or import notebooks manually.
2. Upload `superstore.csv` to `/FileStore/tables/`.
3. Run notebooks in order:
   - `01_bronze_ingest`
   - `02_silver_transform`
   - `03_gold_analytics`
4. Query results with Databricks SQL and create dashboards.

## Extensions
- Add **streaming ingestion** (Auto Loader).
- Integrate **MLflow** for sales forecasting.
- Add **alerting** for low-profit categories.
