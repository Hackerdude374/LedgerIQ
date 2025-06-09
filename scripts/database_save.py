import sqlite3
import os

def save_to_database(df):
    conn = sqlite3.connect(os.path.join("database", "accounting_data.sqlite"))
    df.to_sql("transactions", conn, if_exists="append", index=False)
    conn.close()
