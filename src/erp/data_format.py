import pandas as pd
from utils import load_db_config
from sqlalchemy import create_engine
import datetime as dt

db_config = load_db_config()
db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
engine = create_engine(db_url)

df = pd.read_sql("SELECT * FROM sales", con=engine)

df = df.rename(columns={
"invoice_id": "InvoiceNumber",
"branch": "StoreBranch",
"customer_type": "CustomerCategory",
"total": "TotalAmount",
"date": "TransactionDate"
})

df["TransactionDate"] = pd.to_datetime(df['TransactionDate'])

df["TransactionDate"] = df["TransactionDate"].dt.strftime('%Y-%m-%d')

df.to_csv("data/processed/erp_sales_data.csv", index=False)
print("ERP DATA SAVED")
