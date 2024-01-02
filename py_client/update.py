import requests


endpoint = "http://127.0.0.1:8000/api/product/update/1/"

data = {
    'name':'hai',
    'price':100,
}


get_response =  requests.put(endpoint,json=data)
print(get_response.status_code)
print(get_response.json())