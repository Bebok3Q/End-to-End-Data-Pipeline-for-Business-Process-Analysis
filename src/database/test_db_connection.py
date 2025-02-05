from sqlalchemy import create_engine
from database.utils import load_db_config

def test_db_connection():
    db = load_db_config()

    db_url = f"{db['type']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}"

    try:
        engine = create_engine(db_url)
        conn = engine.connect()
        print("Connection succesfull")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_db_connection()