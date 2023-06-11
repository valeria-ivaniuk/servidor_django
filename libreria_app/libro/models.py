from django.db import models
from autor import models as m

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(m.Autor, on_delete=models.CASCADE)