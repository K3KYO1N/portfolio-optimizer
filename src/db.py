import sqlite3

def get_connection(db_name="portfolio.db"):
    conn = sqlite3.connect(db_name)
    return conn
