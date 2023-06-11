import requests 

endpoint = 'http://127.0.0.1:8000/libro/1'
endpoint_delete = 'http://127.0.0.1:8000/libro/delete/3'
endpoint_add = 'http://127.0.0.1:8000/libro/create'
endpoint_update = 'http://127.0.0.1:8000/libro/update/3'

response = requests.post(endpoint_add, json={'titulo': 'Don Quijote', 'autor': 3})
#response = requests.get(endpoint)
#response = requests.delete(endpoint_delete)
#response = requests.put(endpoint_update, json={'titulo': 'Don Quijote de la Mancha', 'autor': 3})

print(response.json())