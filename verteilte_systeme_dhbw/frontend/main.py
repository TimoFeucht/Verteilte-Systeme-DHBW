import requests

url = 'http://127.0.0.1:8000'
data = {
  "email": "beispiel@beispiel.de",
  "password": "deinPasswort"
}

# response = requests.post(url, json=data)
response = requests.get(url)

print(response.status_code)
print(response.json())
