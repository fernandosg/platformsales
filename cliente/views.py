from django.shortcuts import render
from django.http import JsonResponse
from django.urls import (reverse,reverse_lazy)
from cliente.forms import RegisterCliente
from django.views.generic import (TemplateView, UpdateView)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cliente.models import Cliente
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
class IndexView(PermissionRequiredMixin,ListView):
    permission_required="cliente.root_cliente"
    template_name="cliente/index.html"

    def get_queryset(self):
        return Cliente.objects.filter()

    def get_context_data(self,*args,**kwargs):
        return {"clientes":Cliente.objects.all()}

    def post(self,request,*args,**kwargs):
        return self.get(request,*args,**kwargs)

class ExitoRegistro(TemplateView):
    template_name="cliente/exito.html"

class DetalleClienteView(PermissionRequiredMixin,UpdateView):
    permission_required="cliente.root_cliente"
    template_name="cliente/detalle_cliente.html"
    model=Cliente
    form_class=RegisterCliente
    success_url=reverse_lazy("cliente:index_cliente")

class Register(PermissionRequiredMixin,TemplateView):
    permission_required="cliente.root_cliente"
    template_name="cliente/register.html"

    def dispatch(self,request,*args,**kwargs):
        self.form=RegisterCliente(request.POST or None)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,*args,**kwargs):
        return {"form":self.form}

    def post(self,request, *args, **kwargs):
        if self.form.is_valid():
            cliente=self.form.save()
            return JsonResponse({
                "nombre":cliente.nombre
            })
        return self.get(request,*args,**kwargs)
