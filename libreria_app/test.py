from django.test import TestCase


from rest_framework.test import APIClient
from autor.models import Autor

class AutorViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.autor2 = Autor.objects.create(nombre='J.K', apellido='Rowling')
        self.autor3 = Autor.objects.create(nombre = 'Federico', apellido='Garcia Lorca')
    
    def test_restringir_put(self):
        url = f'/autores/autor_viewset/{self.autor2.id}/'
        data = {'nombre': 'J.K.', 'apellido':'Rowling'}

        response = self.client.put(url,data,format='json')

        self.assertEqual(response.status_code, 405)
