
'''
File name: load_tickers.py
Purpose: Pulls the ticker list from Massive and inserts it into reference.
'''
import time
import sqlite3
import os
from massive import RESTClient

client = RESTClient(api_key=os.environ["MASSIVE_API_KEY"])

conn = sqlite3.connect("data/market.db")
cur = conn.cursor()#writing

TEST_MODE = True

count = 0
for active_flag in [True, False]:
    for t in client.list_tickers(market="stocks", active=active_flag, limit=1000):
        cur.execute(
            "INSERT OR IGNORE INTO reference (ticker, name, type, exchange, active, cik) VALUES(?, ?, ?, ?, ?, ?)",
            (t.ticker, t.name, t.type, t.primary_exchange, 1 if t.active else 0, t.cik)
        )

        count += 1
        
        if TEST_MODE and count % 50 == 0:
            break

        if count % 1000 == 0:
            conn.commit()
            print(count, "rows saved")
            time.sleep(12.5)

conn.commit()
conn.close()
print("done,", count, "rows total")
    