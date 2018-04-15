from django.shortcuts import render
from django.views.generic import CreateView
from usuarios.forms import RegistroForm
from django.urls import reverse_lazy
# Create your views here.

class RegistroUsuario(CreateView):
    template_name="usuarios/registrar.html"
    form_class=RegistroForm
    success_url=reverse_lazy("contratos:index_contrato")
