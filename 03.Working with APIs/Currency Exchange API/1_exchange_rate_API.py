import requests
import json

base_url = "https://api.apilayer.com/exchangerates_data/latest"

payload = {}
headers= {
  "apikey": "XWc9W74Zj5eRLEdY5VzPsmiIXKAHWUUw"
}

#reqeust to API
response = requests.request("GET", base_url, headers=headers, data = payload)

#investigating response
print(response.ok)
print(response.status_code)
print(response.text)

#handling JSON
json_response = response.json()

#Python Built in package json
#loads(string): converts a JSON formatted string to a Python Object
#dumps(obj): converts a Python Object to a regular string, with options to make the string prettier
print(json.dumps(json_response, indent=4))