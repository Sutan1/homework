# I AM USING A PYTEST FOR THIS
import requests
import json

ENDPOINT = "main url"



def test_get_transaction():
    #Login first to obtain the token
    email = 'xxxx@xxxxxxxxx.io'
    password = 'xxxxxxxx'
    payload = {'email': email, 'password': password}
    url_for_log = "endpoint for merchant login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)

    #GET TRANSACTION
    url_get_transaction = "endpoint for a particular transaction info"
    headers_get_transaction = {"Authorization": token}
    payload_get_trasnaction = {"transactionId": "x-xxxxxxxxxx-x"}

    response_get_transaction = requests.post(ENDPOINT + url_get_transaction, headers=headers_get_transaction, params=payload_get_trasnaction)
    assert response_get_transaction.status_code == 200
    
    data_get_transaction = response_get_transaction.json()
    print(data_get_transaction)