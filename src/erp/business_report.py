# Sales summary report
# Customer behavior report
# Process eficiency report
import pandas as pd
from utils import load_db_config
from sqlalchemy import create_engine


db_config = load_db_config()
db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
engine = create_engine(db_url)

df = pd.read_sql("SELECT * FROM sales", con=engine)



with pd.ExcelWriter('reports/sales_analysis.xlsx') as writer:
    # Sales
    df.groupby('branch')['total'].sum().to_excel(writer,sheet_name="Sales by Branch")

    # Customer behavior
    df.groupby('gender')['total'].sum().to_excel(writer, sheet_name="Customer Behavior")

    #Transaction time
    df['hour'] = df['time'].apply(lambda x : x.hour)
    df.groupby('hour')['total'].sum().to_excel(writer, sheet_name="Sales by Hour")

print("REPORTS SAVED")