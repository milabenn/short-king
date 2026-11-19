'''
File name: load_bars.py
Purpose: Pulls daily bars from Massive's grouped daily endpoints 
    and inserts it into daily_bars in market.db.
'''

import sqlite3
import time
from datetime import date, timedelta
import os
from massive import RESTClient

TEST_MODE = True



yesterday = date.today() - timedelta(1)

client = RESTClient(api_key=os.environ["MASSIVE_API_KEY"])

conn = sqlite3.connect("data/market.db")
cur = conn.cursor()



if TEST_MODE == True:
    DAYS_BACK = 5
else:
    DAYS_BACK = 700

# select distinct means only pick one time stamp, 
# no need to load all 5165165165 for ever ticker
cur.execute("SELECT DISTINCT timestamp FROM daily_bars")

# done = a collection of every date finished
done = {row[0] for row in cur.fetchall()}

# date loading stops on(the day of the load)
end = yesterday
# date loading starts with(how many days back you want to load)
start = end - timedelta(days=DAYS_BACK)

count = 0
# end-start returns a tiemdelta, .days makes it a normal interger number
# +1 includes teh satart and end date
for i in range((end - start).days + 1):

    # incriments the days forward
    day = start + timedelta(days=i)
    #formats date in "yyyy-mm-dd"
    date_str = day.isoformat()

    if day.weekday() >= 5 or date_str in done:
        continue

    bars = client.get_grouped_daily_aggs(date_str)

    rows = []
    for bar in bars:
        rows.append((bar.ticker, date_str, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.vwap, bar.transactions))

    
    cur.executemany(
        "INSERT OR IGNORE INTO daily_bars (ticker, timestamp, open, high, low, close, volume, vwap, transactions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        rows
    )

    count += len(rows)
    
    conn.commit()
    print(len(rows), " Rows saved for ", date_str)
    time.sleep(12.5)


conn.commit()
conn.close()

if count == 0:
    print("Everything's already up to date.")
else:
    print("All done for", yesterday,".", count, "Rows saved")



    







    
