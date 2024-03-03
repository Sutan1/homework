# I AM USING A PYTEST FOR THIS
import requests
import json

ENDPOINT = "main url"



def test_transaction_report():
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

    #TRANSACTION REPORT
    url_trasnaction_report = "endpoint for transaction REPORT info"
    header_transaction = {"Authorization": token}
    payload_transaction= {
        "fromDate": "2015-07-01",
        "toDate": "2015-10-01",
        "merchant": x,
        "acquirer": x,
    }
    response_transaction_report = requests.post(ENDPOINT + url_trasnaction_report, headers=header_transaction, params=payload_transaction)
    assert response_transaction_report.status_code == 200
    
    data_transaction_report = response_transaction_report.json()
    print(data_transaction_report)


    