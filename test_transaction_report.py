# I AM USING A PYTEST FOR THIS
import requests
import json

ENDPOINT = "https://sandbox-reporting.rpdpymnt.com"



def test_transaction_report():
    #Login first to obtain the token
    email = 'demo@financialhouse.io'
    password = 'cjaiU8CV'
    payload = {'email': email, 'password': password}
    url_for_log = "/api/v3/merchant/user/login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)

    #TRANSACTION REPORT
    url_trasnaction_report = "/api/v3/transactions/report"
    header_transaction = {"Authorization": token}
    payload_transaction= {
        "fromDate": "2015-07-01",
        "toDate": "2015-10-01",
        "merchant": 1,
        "acquirer": 1,
    }
    response_transaction_report = requests.post(ENDPOINT + url_trasnaction_report, headers=header_transaction, params=payload_transaction)
    assert response_transaction_report.status_code == 200
    
    data_transaction_report = response_transaction_report.json()
    print(data_transaction_report)


    