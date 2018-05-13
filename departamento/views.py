from django.shortcuts import render
from django.http import JsonResponse
from django.urls import (reverse,reverse_lazy)
from departamento.forms import RegisterDepartamento
from django.views.generic import (TemplateView,UpdateView)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from departamento.models import Departamento
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class IndexView(PermissionRequiredMixin,ListView):
    permission_required="departamento.root_departamento"
    template_name="departamento/index.html"
    model=Departamento

class ExitoRegistro(TemplateView):
    template_name="departamento/exito.html"

class DetalleDepartamentoView(PermissionRequiredMixin,UpdateView):
    permission_required="departamento.root_departamento"
    template_name="departamento/detalle_departamento.html"
    model=Departamento
    form_class=RegisterDepartamento
    success_url=reverse_lazy("departamento:index_departamento")

class Register(PermissionRequiredMixin,TemplateView):
    permission_required="departamento.root_departamento"
    template_name="departamento/register.html"

    def dispatch(self,request,*args,**kwargs):
        self.form=RegisterDepartamento(request.POST or None)
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        return {"form":self.form}

    def post(self,request,*args,**kwargs):
        if self.form.is_valid():
            departamento=self.form.save()
            return JsonResponse({"nombre":departamento.nombre})
        return self.get(request,*args,**kwargs)
