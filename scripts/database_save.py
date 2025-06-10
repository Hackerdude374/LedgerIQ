# import sqlite3
# import os

# def save_to_database(df):
#     conn = sqlite3.connect(os.path.join("database", "accounting_data.sqlite"))
#     df.to_sql("transactions", conn, if_exists="append", index=False)
#     conn.close()
from sqlalchemy import create_engine
import os

def save_to_database(df):
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/accounting_data.sqlite")
    engine = create_engine(DATABASE_URL)
    df.to_sql("transactions", engine, if_exists="append", index=False)
