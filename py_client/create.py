import requests


endpoint = "http://127.0.0.1:8000/api/product/create/"

data = {
    'name':'phone',
    'description':'halo',
    'price':500
}

get_response =  requests.post(endpoint,json=data)
print(get_response.status_code)
print(get_response.json())