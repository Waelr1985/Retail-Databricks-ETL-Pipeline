# Sjg80-Databricks_ETL_Pipeline

## Overview

This project is designed to perform ETL (Extract, Transform, Load) operations using Databricks notebooks. It utilizes Delta Lake for efficient data storage, Spark SQL for data transformations, proper error handling, data validation, and visualization of the transformed data.

## Dependencies

- Python 3.x
- Databricks platform
- Spark SQL
- Matplotlib
- Requests library
- Dotenv library

## Project Structure

- `etl_process.py`: Contains code to perform ETL operations.
- `visualization.py`: Includes code for data visualization.
- `README.md`: Project documentation.

## Running the Program

1. Clone the repository locally.
2. Set up the required environment variables using a `.env` file.
3. Open Databricks and create notebooks for `etl_process.py` and `visualization.py`.
4. Run `etl_process.py` to perform ETL operations.
5. Run `visualization.py` to generate visualizations.

### Environment Variables

- `SERVER_HOSTNAME`: Databricks server hostname.
- `ACCESS_TOKEN`: Access token for Databricks API authentication.

## ETL Process

Let's break down each code snippet and its functionality:


### Extraction `extract.py`

The `extract()` function in `etl_process.py` fetches data from a specified URL and stores it in the FileStore.
This Python script extracts a file from a given URL and stores it in the Databricks FileStore using Databricks REST APIs.

- `perform_query`: A utility function that performs HTTP POST requests to the Databricks API.
- `mkdirs`, `create`, `add_block`, `close`: Functions to interact with Databricks File System (DBFS) via REST API.
- `put_file_from_url`: Downloads a file from a given URL, encodes it in base64, and uploads it to the specified DBFS path.
- `extract`: Downloads a CSV file from a URL, stores it in the FileStore at a specific path, and returns the file path.

### 2. Transformation and Loading `transform_load.py`

The `load()` function reads the extracted data, performs schema inference, splits it into two DataFrames, assigns unique IDs, and stores them as Delta tables (`obesity_data1_delta` and `obesity_data2_delta`).

This script uses Apache Spark (PySpark) to load a CSV file from the FileStore, perform data transformation, split it into two DataFrames, assign unique IDs, and write the transformed data into Delta tables.

- `load`: Reads a CSV file using PySpark, splits the columns into two halves, creates two DataFrames, assigns unique IDs, and stores them as Delta tables (`obesity_data1_delta` and `obesity_data2_delta`).

### 3. Visualization `query_viz.py`
The `query_transform()` and `viz()` functions in `visualization.py` perform Spark SQL queries and generate visualizations to analyze average age, height, and weight by gender.

This script uses Spark SQL to perform data querying and generates visualizations using Matplotlib based on the transformed data.

- `query_transform`: Executes a custom SQL query on the loaded data (assumed to be loaded as a DataFrame named `obesity_data`) to calculate average age, height, and weight by gender.
- `viz`: Generates a bar plot visualization showing the average age, height, and weight by gender using Matplotlib.

Overall, these scripts perform a comprehensive ETL process, starting from data extraction, transforming and loading data into Delta tables using PySpark, and finally, querying and visualizing the transformed data using Spark SQL and Matplotlib, respectively.

![image](https://github.com/nogibjj/Sjg80-Databricks_ETL_Pipeline/assets/142270941/237bb68f-3c8f-4f50-9783-a0f85433257b)

## Recommendations

Based on the data analysis:

- There's a notable difference in average height between genders, indicating potential areas for targeted health programs.
- The average weight distribution might suggest a need for gender-specific dietary guidance.

