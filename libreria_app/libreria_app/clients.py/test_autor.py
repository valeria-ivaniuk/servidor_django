import requests 

endpoint = 'http://127.0.0.1:8000/autor/3'
endpoint_delete = 'http://127.0.0.1:8000/autor/delete/2'
endpoint_add = 'http://127.0.0.1:8000/autor/create'
endpoint_update = 'http://127.0.0.1:8000/autor/update/3'
endpoint_api_view = 'http://127.0.0.1:8000/libro'


#response = requests.get(endpoint)
#response = requests.post(endpoint_add, json={'nombre': 'J.K.', 'apellido':'Rowling'})
#response = requests.delete(endpoint_delete)
#response = requests.put(endpoint_update, json={'nombre': 'Miguel', 'apellido':'de Cervantes Saavedra'})
response = requests.get(endpoint_api_view)

print(response.json())