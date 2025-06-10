mkdir bot_dashboard && cd bot_dashboard
mv /storage/emulated/0/Download/bot_dashboard.zip .
unzip bot_dashboard.zip
git init
git add .
git commit -m "Primeiro commit do bot"
git remote add origin https://github.com/Phtrader043/Bot-dashboard-.git
git branch -M main
git push -u origin main
import requests
API_KEY = "SUA_API_KEY"
symbol = "EUR"
to_symbol = "JPY"
url = f"https://min-api.cryptocompare.com/data/v2/histominute"
params = {
}
response = requests.get(url, params=params)
print(response.json())
import requests
API_KEY = "95347293c4d4192e31493eeef320b48502e61438d56678f9684a4d3a7c90112d"
symbol = "EUR"
to_symbol = "JPY"
url = f"https://min-api.cryptocompare.com/data/v2/histominute"
params = {
}
response = requests.get(url, params=params)
print(response.json())
