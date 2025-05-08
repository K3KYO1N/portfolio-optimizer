CREATE TABLE trades (
    id INTEGER PRIMARY KEY,
    date TEXT,
    symbol TEXT,
    action TEXT CHECK(action IN ('BUY', 'SELL')),
    shares INTEGER,
    price REAL
);

CREATE TABLE portfolio (
    symbol TEXT,
    shares INTEGER,
    average_price REAL,
    market_value REAL
);

CREATE TABLE performance (
    date TEXT,
    total_value REAL,
    cash REAL,
    returns REAL
);
