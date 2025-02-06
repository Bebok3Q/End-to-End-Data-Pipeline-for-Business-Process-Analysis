# End-to-End Data Pipeline for Business Process Analysis
This project aims to build an end-to-end data pipeline for analyzing business processes using the Supermarket Sales dataset. The goal is to extract, transform, load (ETL), perform process mining, and generate actionable insights from the data.
# Day 1: Data Extraction & ETL Pipeline
1. Project Setup
Created a GitHub repository and structured the project.
Set up a Python virtual environment with necessary dependencies using requirements.txt.
Downloaded the Supermarket Sales dataset from Kaggle and added it to the data/raw folder.
2. ETL Process
Extracted data from a CSV file (supermarket_sales.csv) using pandas.
Transformed the data by:
Parsing the date and time columns correctly.
Renaming columns for consistency and converting them to lowercase.
Replacing special characters like % in column names.
Ensuring correct data types for all columns.
3. Database Integration
Loaded the transformed data into a PostgreSQL database using SQLAlchemy.
Established the database connection using credentials stored in a .env file.
Inserted the data into a sales table, ensuring the column names matched those in the database.
# Day 2: Process Mining & Data Analysis
1. Event Log Preparation
Extracted relevant data from the database and transformed it into an event log format.
The event log consists of essential columns for analysis, such as Invoice ID, Event Type, Event Time, Branch, Customer Type, Payment, and Total Amount.
2. Process Mining
Utilized the PM4Py library to perform process mining on the sales data.
Analyzed process flows to identify bottlenecks and inefficiencies in the sales process.
Generated PetriNet and BPMN charts.
