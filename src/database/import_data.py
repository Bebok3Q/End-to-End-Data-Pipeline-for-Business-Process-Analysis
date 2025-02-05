import pandas as pd
from database.utils import load_db_config
from sqlalchemy import create_engine


def load_and_insert_data():
    df = pd.read_csv(r"data\raw\supermarket_sales.csv")
    # Date and Time needs to be changed
    df["Date"] = pd.to_datetime(df["Date"], format = '%m/%d/%Y')
    df["Time"] = pd.to_datetime(df["Time"], format='%H:%M').dt.time

    df.columns = df.columns.str.replace(' ', '_').str.lower()
    df = df.rename(columns={'tax_5%': 'tax_5_percent'})


    db_config = load_db_config()
    db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"

    engine = create_engine(db_url)
    conn = engine.connect()

    df.to_sql('sales', con=engine, if_exists='append', index=False)
    print("Inserted the data to sales table")
    conn.close()

if __name__ == "__main__":
    load_and_insert_data()