import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 23.571923,
"longitude": 119.580378,
"current": "temperature_2m",
"timezone": "Asia/Taipei"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status() 

print(response.status_code)
data = response.json()
print(data)

# 1. 先取得第一層 current 字典
current = data["current"]
# 2. 再從 current 中取得目標數值
temperature = current["temperature_2m"]
# 3. 印出結果
print("當前溫度:", temperature)
