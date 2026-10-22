'''
File name: db_init.py
Purpose: Initializes the database.


'''
import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/market.db")# connects to db, if doesnt exist, it makes market.db

cur = conn.cursor()# cursor:the thing that writes in the db

cur.execute("""
CREATE TABLE IF NOT EXISTS daily_bars (
    ticker TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    vwap REAL,
    transactions INTEGER,
    PRIMARY KEY (ticker, timestamp) 
    )
"""
)

cur.execute("CREATE INDEX IF NOT EXISTS idx_bars_date ON daily_bars(timestamp)")#creates date index for scanning by date faster

cur.execute("""
CREATE TABLE IF NOT EXISTS reference (
    ticker TEXT NOT NULL,
    name TEXT, 
    type TEXT, 
    exchange TEXT,  
    active INTEGER, 
    market_cap INTEGER, 
    shares_outstanding INTEGER, 
    cik TEXT,
    PRIMARY KEY (ticker)
)
"""
)

conn.commit()#actually writes it to a db

conn.close()