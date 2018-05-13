from django import forms
from django.forms import ModelForm
from departamento.models import Departamento

class RegisterDepartamento(forms.ModelForm):

    class Meta():
        model=Departamento
        fields=["nombre","edificio"]
