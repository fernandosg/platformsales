from django import forms
from django.forms import ModelForm
from edificio.models import Edificio
class RegisterEdificio(forms.ModelForm):

    class Meta():
        model=Edificio
        fields=["nombre"]
