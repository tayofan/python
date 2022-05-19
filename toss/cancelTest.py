import http.client

conn = http.client.HTTPSConnection("api.tosspayments.com")

payload = "{\"cancelReason\":\"고객이 취소를 원함\"}".encode('utf-8')

headers = {
    'Authorization': "Basic dGVzdF9za19rNmJKWG1nbzI4ZXhtSk1ubjJYckxBbkdLV3g0Og==",
    'Content-Type': "application/json"
    }

conn.request("POST", "/v1/payments/qKl56WYb7w4vZnjEJeQVxYEMKbOEzrPmOoBN0k12dzgRG9px/cancel", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))