from dotenv import load_dotenv
import os
import mysql.connector
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def load_production_data():
    conn = get_connection()

    query = "SELECT * FROM production_data"

    df = pd.read_sql(query, conn)

    conn.close()

    return df