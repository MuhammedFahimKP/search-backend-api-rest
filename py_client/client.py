import requests


endpoint = "http://127.0.0.1:8000/api/"

get_response =  requests.post(endpoint,json={
    "name":"helloworld",
    "description":"hai",
    "price":500,
})
print(get_response.status_code)
print(get_response.json())