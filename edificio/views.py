from django.shortcuts import render
from django.http import JsonResponse
from django.urls import (reverse,reverse_lazy)
from edificio.forms import RegisterEdificio
from django.views.generic import TemplateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from edificio.models import Edificio
from departamento.models import Departamento
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
class IndexView(PermissionRequiredMixin,ListView):
    permission_required="edificio.root_edificio"
    template_name="edificio/index.html"
    model=Edificio

class ExitoRegistro(TemplateView):
    template_name="edificio/exito.html"

class DetalleEdificioView(PermissionRequiredMixin, UpdateView):
    permission_required="edificio.root_edificio"
    template_name="edificio/detalle_edificio.html"
    model=Edificio
    form_class=RegisterEdificio
    success_url=reverse_lazy("edificio:index_edificio")

class Register(PermissionRequiredMixin,TemplateView):
    template_name="edificio/register.html"
    permission_required="edificio.root_edificio"

    def dispatch(self,request,*args,**kwargs):
        self.form=RegisterEdificio(request.POST or None)
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        return {"form":self.form}

    def post(self,request,*args,**kwargs):
        if self.form.is_valid():
            edificio=self.form.save()
            print("FUE valido")
            return JsonResponse({"nombre":edificio.nombre})
        print("NO FUE VALIDO :(!!!")
        return self.get(request,*args,**kwargs)
