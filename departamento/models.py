from django.db import models
from edificio.models import Edificio
# Create your models here.
class Departamento(models.Model):
    nombre=models.CharField(max_length=50)
    edificio=models.ForeignKey(Edificio,on_delete=models.CASCADE,related_name="edificio")
    def __str__(self):
        return self.nombre
