from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,UpdateView)
from django.http import JsonResponse
from django.urls import reverse_lazy
from contratos.forms import CrearContrato
from contratos.models import Contrato
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class IndexView(PermissionRequiredMixin,ListView):
    permission_required="contratos.root_contrato"
    template_name="contratos/index.html"
    model=Contrato

class Crear(PermissionRequiredMixin,TemplateView):
    permission_required="contratos.root_contrato"
    template_name="contratos/crear.html"
    def dispatch(self,request,*args,**kwargs):
        self.form=CrearContrato(request.POST or None)
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        return {"form":self.form}

    def post(self,*args,**kwargs):
        if self.form.is_valid():
            contrato=self.form.save()
            return JsonResponse({
                "fecha_instalacion":contrato.fecha_instalacion
            })
        return self.get(request,*args,**kwargs)

class DetalleContrato(PermissionRequiredMixin,UpdateView):
    permission_required="contratos.root_contrato"
    template_name="contratos/detalle_contrato.html"
    model=Contrato
    form_class=CrearContrato
    success_url=reverse_lazy("contratos:index_contrato")
