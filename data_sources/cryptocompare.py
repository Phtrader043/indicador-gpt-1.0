import requests

CRYPTOCOMPARE_API_KEY = "02816cb2d68aafdda6b92cc525cdcaf663f780978c30d9e5429d6712a52cfdff"

def get_crypto_data(symbol="BTC", market="USD", limit=30):
    url = f"https://min-api.cryptocompare.com/data/v2/histominute?fsym={symbol}&tsym={market}&limit={limit}&api_key={CRYPTOCOMPARE_API_KEY}"
    r = requests.get(url)
    return r.json()["Data"]["Data"]
