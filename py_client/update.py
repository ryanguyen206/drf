import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": 'Updated field',
    "price": '69.00'
}

get_response = requests.put(endpoint, json=data)

print(get_response.status_code)