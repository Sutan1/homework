# I AM USING A PYTEST FOR THIS
import requests

ENDPOINT = "https://sandbox-reporting.rpdpymnt.com"



def test_merchant_login():
    email = 'demo@financialhouse.io'
    password = 'cjaiU8CV'
    payload = {'email': email, 'password': password}
    url_for_log = "/api/v3/merchant/user/login"
    
    response_merchant_login = requests.post(ENDPOINT + url_for_log, data=payload)
    token = response_merchant_login.json()['token'] 
    assert response_merchant_login.status_code == 200
    
    data_merchant_for_login = response_merchant_login.json()
    print(data_merchant_for_login)