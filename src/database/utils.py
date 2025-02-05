from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv("config/.env")

def load_db_config():
    db_config = {
        "type": os.getenv("DB_TYPE"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "name": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    return db_config


def get_db_connection():
    """Establish a database connection using SQLAlchemy"""
    db = load_db_config()
    db_url = f"{db['type']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}"
    
    try:
        engine = create_engine(db_url)
        connection = engine.connect()
        print("Successfully connected to the database!")
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None