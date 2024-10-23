import requests

endpoint = "http://localhost:8000/api/products/"

# get_response = requests.get(endpoint, params={"abc":123}, json={"query": "Hello World"}) # HTTP Request
get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"})

# print(get_response.text) #Print raw text response
print(get_response.status_code)
print(get_response.json()) #get json response sent from endpoint