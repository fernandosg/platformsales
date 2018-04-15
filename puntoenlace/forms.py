from django import forms
from django.forms import ModelForm
from puntoenlace.models import PuntoEnlace

class CrearPuntoEnlace(forms.ModelForm):

    class Meta():
        model=PuntoEnlace
        fields=["nombre"]
