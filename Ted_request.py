import http.client

conn = http.client.HTTPSConnection("10.246.155.71", 9020)
payload = ''
headers = {
    'X-Amz-Date': '20201218T170758Z',
    'Authorization': 'AWS4-HMAC-SHA256 Credential=tp-user01/20201218/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=634ec3c7f269a53a808c73aa3bb57482b730678b7d5486434abbe0d3329d207a'
}
conn.request("GET", "/versioning-bucket01", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))