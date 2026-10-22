import os

from massive import RESTClient

client = RESTClient(api_key=os.environ["MASSIVE_API_KEY"])




for t in client.list_tickers(market="stocks", active=True, limit=1000):
    print(t)
    break