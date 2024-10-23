import requests

endpoint = "http://localhost:8000/products/2/"
endpoint2 = "http://localhost:8000/products/"

data = {
    "title": "Realme P1"
}


get_response = requests.get(endpoint)
create_a_thingy = requests.post(endpoint2, json=data)

# print(get_response.json())

print(create_a_thingy)