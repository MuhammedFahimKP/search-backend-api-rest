import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint,json={
    'username':'f12345',
    'password':password
})

print(auth_response.json())

if auth_response.status_code == 200:

    token = auth_response.json()['token']

    headers = {

        'Authorization': f'Token {token}'
    }

    endpoint = "http://127.0.0.1:8000/api/product/list-create/"
    data = {
            'name':'Muhammed Fahim',
            'description':'sony',
            'price':700
    }

       
    get_response =  requests.get(endpoint,headers=headers)
    print(get_response.status_code)
    data = get_response.json()
    nex_url = data['next']
    print(data)
    print(nex_url)

    if nex_url is not None:
        get_response =  requests.get(endpoint,headers=headers)
        print(get_response.json())
        


