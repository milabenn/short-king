import os
import utils.py as utils

from massive import RESTClient

client = RESTClient(api_key=os.environ["MASSIVE_API_KEY"])

for bar in client.list_aggs("AAPL", 1, "day", "2026-10-01", "2026-10-08"):
    print(bar) 

details = client.get_previous_close_agg("AAPL")
print("hello world")