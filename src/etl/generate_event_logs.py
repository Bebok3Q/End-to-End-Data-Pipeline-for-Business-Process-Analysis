import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from utils import load_db_config






# I have to generate event logs by myself, as my db doesn't have this type of info
def generate_event_logs():

    db_config = load_db_config()
    db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
    engine = create_engine(db_url)

    df = pd.read_sql("SELECT * FROM sales", con=engine)

    event_log = []
    
    for _,row in df.iterrows():
        invoice_id = row['invoice_id']
        branch = row['branch']
        customer_type = row['customer_type']
        payment_method = row['payment']
        event_time = datetime.combine(row['date'], row['time'])
        total_amount = row['total']

        # SImulate the process
        event_log.append([invoice_id, "Customer Entry", event_time - timedelta(minutes=10), branch, customer_type, payment_method, total_amount])
        event_log.append([invoice_id, "Product Browsing", event_time - timedelta(minutes=5), branch, customer_type, payment_method, total_amount])
        event_log.append([invoice_id, "Checkout", event_time, branch, customer_type, payment_method, total_amount])
        event_log.append([invoice_id, "Payment Processed", event_time + timedelta(minutes=1), branch, customer_type, payment_method, total_amount])
        event_log.append([invoice_id, "Transaction Completed", event_time + timedelta(minutes=2), branch, customer_type, payment_method, total_amount])

    event_df = pd.DataFrame(event_log, columns=['case_id', 'event_name', 'event_timestamp', "branch", "customer_type", "payment_method", "total_amount"])

    event_df.to_sql("event_logs", con=engine, if_exists='append', index=False)
    print("Event log generated in db")







if __name__ == '__main__':


    generate_event_logs()