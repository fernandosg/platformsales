from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,UpdateView)
from reportes.forms import CrearReporte
from reportes.models import MensajeOperacion
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class IndexView(ListView):
    template_name="reportes/index.html"
    model=MensajeOperacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Crear(PermissionRequiredMixin,TemplateView):
    permission_required="reportes.root_reporte"
    template_name="reportes/crear.html"

    def dispatch(self,request,*args,**kwargs):
        self.form=CrearReporte(request.POST or None)
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        return {"form":self.form}

    def post(self,*args,**kwargs):
        if(self.form.is_valid()):
            reporte=self.form.save()
            return JsonResponse({
                "mensaje":reporte.mensaje
            })
        return self.get(request,*args,**kwargs)

class EditarReporte(PermissionRequiredMixin,UpdateView):
    permission_required="reportes.root_reporte"
    template_name="reportes/editar_reporte.html"
    model=MensajeOperacion
    form_class=CrearReporte
    success_url=reverse_lazy("reportes:index_reporte")
