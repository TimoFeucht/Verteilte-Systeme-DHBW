import requests

# example usage of requests

url = 'http://127.0.0.1:8000'
url1 = 'http://127.0.0.1:8000/connect/'
url2 = 'http://127.0.0.1:8000/question/'

data2 = {
    "user_id": 1
}

# response = requests.get(url)
# response = requests.post(url1)
response = requests.get(url2, params=data2)

print(response.status_code)
print(response.json())
