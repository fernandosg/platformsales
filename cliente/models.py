from django.db import models
from puntoenlace.models import PuntoEnlace
from django.contrib.auth.models import User
# Create your models here.
class Departamento(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido_paterno=models.CharField(max_length=50)
    apellido_materno=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=12)
    fecha_instalacion=models.DateTimeField()
    is_activo=models.BooleanField(default=True)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE,related_name="departamentos")
    puntoenlace=models.ForeignKey(PuntoEnlace,on_delete=models.CASCADE,related_name="puntoenlaces")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="useradmin")

    def __str__(self):
        return self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno

class PagoCliente(models.Model):
    fecha_pago=models.DateTimeField()
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="clientes")

    def __str__(self):
        return str(self.cliente)
