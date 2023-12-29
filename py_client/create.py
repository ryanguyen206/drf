import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "gucci gang"
}

get_response = requests.post(endpoint, json= data)

print(get_response.json())