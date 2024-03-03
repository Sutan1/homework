import requests

ENDPOINT = "https://sandbox-reporting.rpdpymnt.com"


email = 'demo@financialhouse.io'
password = 'cjaiU8CV'
payload = {'email': email, 'password': password}


def test_login_for_merchant():
    url_for_log = "/api/v3/merchant/user/login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)
    print(token)

def test_transaction_report():
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

def test_get_transaction():
    url_get_transaction = "/api/v3/transaction"
    headers_get_transaction = {"Authorization": token}
    payload_get_trasnaction = {"transactionId": "1-1444392550-1"}

    response_get_transaction = requests.post(ENDPOINT + url_get_transaction, headers=headers_get_transaction, params=payload_get_trasnaction)
    assert response_get_transaction.status_code == 200
    
    data_get_transaction = response_get_transaction.json()
    print(data_get_transaction)

def test_get_client():
    url_get_client = "/api/v3/client"
    headers_get_client = {"Authorization": token}
    payload_get_client = {"transactionId": "1-1444392550-1"}

    response_get_client = requests.post(ENDPOINT + url_get_client, headers = headers_get_client, params = payload_get_client)
    assert response_get_client.status_code == 200
    
    data_get_client = response_get_client.json()
    print(data_get_client)