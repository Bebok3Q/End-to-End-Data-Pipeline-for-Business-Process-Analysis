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

### **✅ 1: Data Extraction & ETL Pipeline**

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

### **✅ 2: Process Mining & Insights**

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

### **✅ 3: ERP Integration & Reporting**

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

