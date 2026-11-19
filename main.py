import os

from massive import RESTClient

client = RESTClient(api_key=os.environ["MASSIVE_API_KEY"])



grouped_aggs = client.get_grouped_daily_aggs(date="2026-04-07")

print (grouped_aggs)
