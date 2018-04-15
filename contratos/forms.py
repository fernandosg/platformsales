from django import forms
from contratos.models import Contrato
class CrearContrato(forms.ModelForm):

    class Meta():
        model=Contrato
        fields=["fecha_instalacion","fecha_cobro","estado_contrato","cliente"]
