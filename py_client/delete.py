import requests

endpoint = "http://127.0.0.1:8000/api/product/delete/20/"

data = {
    'name':'hai',
    'price':100,
}


get_response =  requests.delete(endpoint)
print(get_response.status_code)
