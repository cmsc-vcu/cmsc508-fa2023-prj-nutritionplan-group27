import json;
import requests;

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

endpoint = "https://api.edamam.com/api/recipes/v2"
app_key = "a4c54dab3f9f31f1eb0c8a037c8b187e"
app_id = "38724b7d"

def make_parameters(search):
    return {
        "type": "public",
        "q": search,
        "app_id": app_id,
        "app_key": app_key
    }

params = make_parameters("vegetarian")
response = requests.get(endpoint, params=params)

with open("src/api/json/"+params["q"]+".json", 'x', encoding="utf-16") as f:
    f.write(response.text)
