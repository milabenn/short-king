# short-king
Stock screening and shorting Algorithm

## SETUP
1. Set up Massive API free tier account, find your key, copy
2. With your key run in your project terminal:
  * Windows CMD: set MASSIVE_API_KEY=**paste-key-here**
  * Windows PowerShell: $env: MASSIVE_API_KEY="**paste-key-here**" 
  * Mac OS: export MASSIVE_API_KEY="**paste-key-here**"
3. Run File: **db_init.py**
4. Run File: **load_tickers.py**
5. Run File: **load_bars.py**
Note: load_bars and load_tickers both have TEST_MODE set to True at the top, 
simply set it to False to load the whole dataset.
