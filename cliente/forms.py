from django import forms
from django.forms import ModelForm
from cliente.models import Cliente

class RegisterCliente(forms.ModelForm):

    class Meta():
        model=Cliente
        fields=["nombre","apellido_paterno","apellido_materno","correo","telefono","contrasena","fecha_instalacion","is_activo","departamento","puntoenlace"]
