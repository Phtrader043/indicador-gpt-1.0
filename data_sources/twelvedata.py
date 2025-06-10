import requests

TWELVE_DATA_API_KEY = "cd52d4f5c5924063a7af0070445d2a3b"

def get_forex_data(pair="EUR/USD"):
    url = f"https://api.twelvedata.com/time_series?symbol={pair}&interval=1min&apikey={TWELVE_DATA_API_KEY}&outputsize=5"
    r = requests.get(url).json()
    if "values" in r:
        return r["values"]
    return []
