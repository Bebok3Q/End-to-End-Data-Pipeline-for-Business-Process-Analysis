
# End-to-End Data Pipeline for Business Process Analysis

This project aims to build an end-to-end data pipeline for analyzing business processes using the Supermarket Sales dataset. The goal is to extract, transform, load (ETL), perform process mining, and generate actionable insights from the data.

# 1: Data Extraction & ETL Pipeline

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

# 2: Process Mining & Data Analysis

1. Event Log Preparation
   Extracted relevant data from the database and transformed it into an event log format.
   The event log consists of essential columns for analysis, such as Invoice ID, Event Type, Event Time, Branch, Customer Type, Payment, and Total Amount.
2. Process Mining
   Utilized the PM4Py library to perform process mining on the sales data.
   Analyzed process flows to identify bottlenecks and inefficiencies in the sales process.
   Generated PetriNet and BPMN charts.
3. Insights & Visualization
   Generated statistics and visualized key insights using matplotlib and seaborn.
   Focused on analyzing customer behavior, transaction times, and peak sales hours. How should i do it
   ===================================================================================================

# 📊 End-to-End Data Pipeline for Business Process Analysis

## 📌 **Project Overview**

This project implements a complete **ETL pipeline** and **business process analysis** using the  **Supermarket Sales Dataset** . It includes:

* **Data extraction, transformation, and loading (ETL)**
* **SQL-based analysis & insights**
* **Process mining for transaction flow analysis**
* **Data visualization and reporting**
* **ERP integration for business insights**

## 🚀 **Project Structure**

```
End-to-End-Data-Pipeline-for-Business-Process-Analysis/
│-- data/                     # Raw and processed data
│   ├── raw/                  # Original dataset
│   ├── processed/            # Cleaned & transformed data
│-- reports/                  # Generated reports and dashboards
│-- src/                      # Source code
│   ├── etl/                  # ETL pipeline scripts
│   ├── database/             # Process mining analysis
│   ├── erp/                  # ERP data formatting
│-- README.md                 # Project documentation
```

---

## 📅 **Progress Overview**

### **✅ Day 1: Data Extraction & ETL Pipeline**

**Tasks Completed:**

* Set up project structure & GitHub repository
* Loaded **Supermarket Sales** dataset into **PostgreSQL**
* Cleaned and transformed data:
  * Converted **date/time** columns
  * Standardized column names & categorical values
* Extracted key **business insights** using SQL:
  * Total revenue per branch
  * Popular payment methods
  * Peak sales hours

### **✅ Day 2: Process Mining & Insights**

**Tasks Completed:**

* Generated **event logs** from sales transactions
* Conducted **process mining analysis** using `pm4py`:
  * Identified customer entry & checkout flow
  * Analyzed transaction delays and bottlenecks
* Created **visualizations** using `matplotlib` and `seaborn`:
  * Sales trends over time
  * Payment method distribution
  * Sales performance by product line
* Finalized **business process insights**

### **✅ Day 3: ERP Integration & Reporting**

**Tasks Completed:**

* Formatted data for **ERP system integration**
* Generated structured **invoice logs** for SAP
* Created **business reports** (Excel)
* Built a **summary dashboard** with key metrics
* Finalized project documentation & presentation

---

## 📊 **Key Visualizations & Insights**

✔️ **Total Sales by Branch** (Bar Chart)

✔️ **Sales Distribution by Product Line** (Boxplot)

✔️ **Payment Method Usage** (Pie Chart)

✔️ **Sales Trends Over Time** (Line Chart)

🔗 **Dashboard Screenshot:** `reports/sales_dashboard.png`

---

## 🛠 **Technologies Used**

* **Python** (Pandas, NumPy, SQLAlchemy, Matplotlib, Seaborn)
* **SQL** (PostgreSQL for data storage & queries)
* **Process Mining** (PM4Py)
* **Data Visualization** (Matplotlib, Power BI, Excel)
* **ERP Data Formatting** (SAP-compatible structure)

---

## 📥 **How to Run the Project**

1. Clone this repository:
   ```sh
   git clone https://github.com/Bebok3Q/End-to-End-Data-Pipeline-for-Business-Process-Analysis.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the ETL pipeline:
   ```sh
   python src/etl/load_and_insert_data.py
   ```
4. Create final reports & visualizations:
   ```sh
   python src/erp/data_format.py
   python src/erp/summary.py
   ```

>>>>>>> c0a301f (Finalized reporting, ERP integration, and documentation)
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>
