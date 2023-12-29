import requests

product_id = input("product id")

try:
    product_id = int(product_id)
except:
    pass

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

print(endpoint)

get_response = requests.delete(endpoint)

print(get_response.json())