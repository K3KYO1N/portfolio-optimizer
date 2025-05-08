import yfinance as yf
import pandas as pd
from src.db import get_connection

def simulate_trade(symbol, action, shares, date):
    conn = get_connection()
    cur = conn.cursor()
    
    price = yf.download(symbol, start=date, end=date)['Close'].iloc[0]
    
    cur.execute("INSERT INTO trades (date, symbol, action, shares, price) VALUES (?, ?, ?, ?, ?)",
                (date, symbol, action, shares, price))
    
    conn.commit()
    conn.close()
    return price
