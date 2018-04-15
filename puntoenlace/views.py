from django.shortcuts import render
from puntoenlace.forms import CrearPuntoEnlace
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
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
