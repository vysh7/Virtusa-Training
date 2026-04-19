import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            humidity REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def store_data(city, temp, humidity):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO weather (city, temperature, humidity) VALUES (?, ?, ?)",
        (city, temp, humidity)
    )

    conn.commit()
    conn.close()


def get_data(city):
    conn = sqlite3.connect('weather.db')

    query = f"SELECT * FROM weather WHERE city='{city}'"
    df = pd.read_sql_query(query, conn)

    conn.close()
    return df