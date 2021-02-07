import requests,json

r = requests.get('http://localhost:9000/')
response = r.content.decode()
# state = json.loads(r.text)
print(response)