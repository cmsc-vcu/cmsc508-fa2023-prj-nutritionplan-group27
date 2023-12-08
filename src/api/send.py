import requests, sys, pandas

url = 'http://localhost:5000'

if len(sys.argv) >= 2:
    url += sys.argv[1]

headers = {
    'username': 'tester',
    'password': 'test',
    'search': 'Steak',
    'exclude': 'True'
    }

print(headers)

response = requests.get(url, headers=headers)

print(response.json())