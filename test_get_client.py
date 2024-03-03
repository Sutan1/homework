# I AM USING A PYTEST FOR THIS
import requests
import json

ENDPOINT = "main url"



def test_get_client():
    #Login first to obtain the token
    email = 'xxxx@xxxxxxxxx.io'
    password = 'xxxxxxxx'
    payload = {'email': email, 'password': password}
    url_for_log = "endpoint fro merchant login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)

    #GET CLIENT
    url_get_client = "endpoint for client info"
    headers_get_client = {"Authorization": token}
    payload_get_client = {"transactionId": "x-xxxxxxxxxx-x"}

    response_get_client = requests.post(ENDPOINT + url_get_client, headers = headers_get_client, params = payload_get_client)
    assert response_get_client.status_code == 200
    
    data_get_client = response_get_client.json()
    print(data_get_client)