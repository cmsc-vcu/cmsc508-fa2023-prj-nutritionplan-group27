import requests, sys

url = 'http://localhost:5000'

if len(sys.argv) >= 2:
    url += sys.argv[1]

headers = {
    'username': 'dellimorez',
    'password': 'password1',
    'name': 'your-recipe-name',
    'calories': '123',
    'ingredients': 'lorem ipsum',
    'instructions': 'dolar sit'
    }

print(headers)

response = requests.get(url, headers=headers)

print(response.json())