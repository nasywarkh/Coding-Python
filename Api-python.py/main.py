import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)

print(response)

data = response.json()
print(type(data))

for todo in data:
    if todo["completed"] == True:
        json_obj = json.dumps(todo, indent=4)
        print(json_obj)
