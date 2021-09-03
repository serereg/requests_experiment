import json
import requests


url = "http://localhost:5000/items/1"
data = {}
params = {'q1': 1, 'q2': 2}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, params=params, data=json.dumps(data), headers=headers)
print(r)

