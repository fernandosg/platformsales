from django.db import models
from cliente.models import Cliente
# Create your models here.
class Contrato(models.Model):
    fecha_instalacion=models.DateTimeField()
    fecha_cobro=models.DateTimeField()
    estado_contrato=models.BooleanField(default=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="clientes_contrato")

    def __str__(self):
        return str(self.cliente)+" "+str(self.fecha_instalacion)
