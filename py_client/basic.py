import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={'123': '456'}, json={"query": 'ay'})

print(get_response.text)