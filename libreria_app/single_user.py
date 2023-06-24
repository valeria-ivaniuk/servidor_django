import requests

endpoint = 'http://127.0.0.1:8000/autores/'

res = requests.get(endpoint)

print(res.json())