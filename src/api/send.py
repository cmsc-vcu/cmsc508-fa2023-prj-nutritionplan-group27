import requests, sys

url = 'http://localhost:5000'

if len(sys.argv) >= 2:
    url += sys.argv[1]

headers = {
    'username': 'dellimorez',
    'password': 'password1',
    'goal-id': '1'
    }

print(headers)

response = requests.get(url, headers=headers)

print(response.json())