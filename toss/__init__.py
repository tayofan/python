from flask import Flask, render_template, request
import requests
import json
from flask.json import jsonify
import http.client
app = Flask(__name__)

@app.route('/order')
def order():
    return render_template('cancel.html')

@app.route('/success')
def success():
    paymentKey = request.args.get('paymentKey', "")
    orderId = request.args.get('orderId', "")
    amount = request.args.get('amount', "")

    url = "https://api.tosspayments.com/v1/payments/"+paymentKey
    params = {'orderId': orderId, 'amount': amount}
    headers = {'Authorization': 'Basic dGVzdF9za19rNmJKWG1nbzI4ZXhtSk1ubjJYckxBbkdLV3g0Og==',
               'Content-Type': 'application/json'}
    res = requests.post(url, data=json.dumps(params), headers=headers)

    print('## URL : ', res.request.url)
    print('## 요청헤더 : ', res.request.headers)
    print('## 요청보디 : ', res.request.body)
    print('## 요청결과 : ', res.text)

    return render_template('success.html', result=res.json(), paymentKey=paymentKey)

@app.route('/cancel')
def cancel():
    conn = http.client.HTTPSConnection("api.tosspayments.com")
    paymentKey = request.args.get('paymentKey')
    payload = "{\"cancelReason\":\"고객이 취소를 원함\"}".encode('utf-8')
    
    headers = {
        'Authorization': "Basic dGVzdF9za19rNmJKWG1nbzI4ZXhtSk1ubjJYckxBbkdLV3g0Og==",
        'Content-Type': "application/json"
        }
    
    conn.request("POST", "/v1/payments/{}/cancel".format(paymentKey), payload, headers)
    
    res = conn.getresponse()
    data = res.read()
    
    print(data.decode("utf-8"))
    return render_template('cancel.html',data=data.decode("utf-8"), paymentKey=paymentKey)    
