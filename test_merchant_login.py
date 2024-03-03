# I AM USING A PYTEST FOR THIS
import requests
import json

ENDPOINT = "main url"



def test_merchant_login():
    email = 'xxxx@xxxxxxxxx.io'
    password = 'xxxxxxxx'
    payload = {'email': email, 'password': password}
    url_for_log = "endpoint for merchant login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)