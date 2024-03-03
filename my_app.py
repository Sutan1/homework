from flask import Flask, jsonify
import json
import requests
import pandas as pd

app = Flask(__name__)

port = 5000

url_main = "https://sandbox-reporting.rpdpymnt.com"


#MERCHANT LOGIN
@app.route("/merchant/user/login")

def merchant_login():
    url_merchant_login = "https:/api/v3/merchant/user/login"
    email = str(input("Enter your email: "))
    password = str(input("Enter your passord: "))
    payload = {'email': email, 'password': password}
    
    response_merchant_login = requests.post(url_main + url_merchant_login, data = payload)
    if response_merchant_login:
        print('APPROVED!')
        token = response_merchant_login.json()['token']
        print(f"Your token : {token}")
        print("Your token is valid for 10 minutes!")
    else:
        return ("Login failed! Status code:", response_merchant_login.status_code)



#TRANSACTION REPORT
@app.route('/trasaction/report')
def get_transaction_report():
    url_transaction_report = "/api/v3/transactions/report"
    headers = {"Authorization": token}
    
    year_from = str(input("Please enter year of the first date, Format 'YYYY': "))
    month_from = str(input("Please enter month of the first date, Format 'MM':: "))
    day_from= str(input("Please enter day of the first date, Format 'dd':: "))
    from_date = year_from + "+" + month_from + "+" + day_from
    from_date_ok = datetime.strptime(to_date, '%Y-%m-%d')
    
    year_to = str(input("Please enter year of the last date, Format 'YYYY': "))
    month_to= str(input("Please enter month of the last date, Format 'MM': "))
    day_to = str(input("Please enter day of the last date, Format 'dd': "))
    to_date = year_to + "+" + month_to + "+" + day_to
    to_date_ok = datetime.strptime(to_date, '%Y-%m-%d') 
    
    merchant_id_transaction_report= int(input("Please enter id of a merchant: "))
    acquirer_id_transaction_report = int(input("Please enter id of a acquirer: "))
               
    payload = {
    "fromDate": from_date_ok,
    "toDate": to_date_ok,
    "merchant": merchant_id_transaction_report ,
    "acquirer": acquirer_id_transaction_report,
}
    response_transaction_report = requests.post(url_main + url_transaction_report, headers = headers, params = payload)
    return response_transaction_report.json()


#GET TRANSACTION
@app.route('/transaction')
def get_transaction():
    url_get_transaction = "/api/v3/transaction"
    headers = {"Authorization": token}
    transaction_id_get_transaction = str(input("Please enter the transaction ID, Format 'x-xxxxxxxxxx-x': "))
    payload = {"transactionId": transaction_id_get_transaction}

    response_get_transaction = requests.post(url_main + url_get_transaction, headers = headers, params = payload)
    return response_get_transaction.json()
    


#GET CLIENT
@app.route('/client')
def photos():
    url_for_client = "https://sandbox-reporting.rpdpymnt.com/api/v3/client"
    headers = {"Authorization": token}
    transaction_get_client = str(input("Please enter a transaction ID, Format 'xxx-xxxxxxxxxx-x': "))
    payload = {"transactionId": transaction_get_client}

    response_get_client = requests.post(url_main + url_for_client, headers = headers, params = payload)

    return response_get_client.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)