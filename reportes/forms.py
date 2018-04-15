from django import forms
from reportes.models import MensajeOperacion
class CrearReporte(forms.ModelForm):

    class Meta():
        model=MensajeOperacion
        fields=["mensaje","estado"]
