import http.client
conn = http.client.HTTPSConnection("10.192.11.180:4443")
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'host': "10.192.11.180:4443",
    'x-amz-date': "20201213T182436Z",
    'authorization': "Basic {{  base64 encoded auth }}",
    'cache-control': "no-cache",
    'postman-token': "20e66407-f2b3-4a4e-e785-6e166ce67db6"
    }
conn.request("GET", "/login", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
