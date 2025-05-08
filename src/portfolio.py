def get_portfolio_value():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM trades", conn)
    
    if df.empty:
        return 0
    
    grouped = df.groupby(['symbol', 'action']).agg({'shares': 'sum', 'price': 'mean'}).reset_index()
    
    # For simplicity, assume all shares are held
    value = 0
    for _, row in grouped.iterrows():
        current_price = yf.download(row['symbol'], period="1d")['Close'].iloc[0]
        value += row['shares'] * current_price
    
    conn.close()
    return value
