from django.db import models
from django.utils import timezone

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    fecha_apertura = models.DateTimeField()

    @property
    def dias_abierta(self):
        dias_abiertos = (timezone.now() - self.fecha_apertura).days
        return dias_abiertos
