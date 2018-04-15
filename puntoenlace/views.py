from django.shortcuts import render
from puntoenlace.forms import CrearPuntoEnlace
from puntoenlace.models import PuntoEnlace
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import (TemplateView,ListView,UpdateView)
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class IndexView(PermissionRequiredMixin,ListView):
    permission_required="puntoenlace.root_puntoenlace"
    template_name="puntoenlace/index.html"
    model=PuntoEnlace

class Crear(PermissionRequiredMixin,TemplateView):
    permission_required="puntoenlace.root_puntoenlace"
    template_name="puntoenlace/crear.html"

    def dispatch(self,request,*args,**kwargs):
        self.form=CrearPuntoEnlace(request.POST or None)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        return {"form":self.form}

    def post(self,*args,**kwargs):
        if self.form.is_valid():
            puntoenlace=self.form.save()
            return JsonResponse({
                "nombre":puntoenlace.nombre
            })
        return self.get(request,*args,**kwargs)

class EditarView(PermissionRequiredMixin,UpdateView):
    permission_required="puntoenlace.root_puntoenlace"
    template_name="puntoenlace/editar.html"
    model=PuntoEnlace
    form_class=CrearPuntoEnlace
    success_url=reverse_lazy("puntoenlace:index_puntoenlace")
