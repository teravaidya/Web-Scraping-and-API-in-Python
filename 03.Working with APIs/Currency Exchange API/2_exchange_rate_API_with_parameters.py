import requests
import json

base_url = "https://api.apilayer.com/exchangerates_data/latest"

param_url = base_url + '?symbols=USD, GBP'

payload = {}
headers = {
	"apikey": "XWc9W74Zj5eRLEdY5VzPsmiIXKAHWUUw"
}

#request to API
response = requests.request("GET", param_url, headers=headers, data=payload)
data = response.json()

#investigating response
print(response.ok)
print(response.status_code)
print(response.text)

print(type(data))
print(data)

rates = data['rates']['USD']
print(rates)