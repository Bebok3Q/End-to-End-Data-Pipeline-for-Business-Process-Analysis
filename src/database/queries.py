import psycopg2
import pandas as pd
from utils import load_db_config

db_config = load_db_config()


def get_top_selling_products():
    query = """
SELECT product_line, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_line
ORDER BY total_quantity DESC;
"""
    return query

def get_total_sales_by_branch():
    query = """
SELECT branch, SUM(quantity) AS total_quantity
FROM sales
GROUP BY branch
ORDER BY total_quantity DESC;
"""
    return query

def get_peak_sales_hours():
    query = """
SELECT EXTRACT(HOUR FROM time)::INT AS hour, SUM(quantity) AS total_quantity
FROM sales
GROUP BY hour
ORDER BY total_quantity DESC;
"""
    return query

def get_branch_analysis():
    query = """
SELECT branch, SUM(gross_income) as total_income
FROM sales
GROUP BY branch
ORDER BY total_income DESC;
"""
    return query


try:
    conn = psycopg2.connect(
        dbname = db_config["name"],
        user = db_config["user"],
        password = db_config["password"],
        host = db_config["host"],
        port = db_config["port"]
    )
    print("DATABASE CONNECTED")

    query = get_top_selling_products()
    df = pd.read_sql(query, conn)
    print(df)

    query = get_total_sales_by_branch()
    df = pd.read_sql(query, conn)
    print(df)

    query = get_peak_sales_hours()
    df = pd.read_sql(query, conn)
    print(df)

    query = get_branch_analysis()
    df = pd.read_sql(query, conn)
    print(df)


finally:
    if conn:
        conn.close()
        print("DATABASE CONNECTION CLOSED")
