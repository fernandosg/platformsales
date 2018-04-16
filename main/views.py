from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models.functions import ExtractMonth
from cliente.models import (PagoCliente,Cliente)
from contratos.models import Contrato
from datetime import datetime
import calendar

# Create your views here.
class LoginUser(TemplateView):
    template_name="main/login.html"

class IndexView(TemplateView):
    template_name="main/index.html"

    def get_context_data(self,*args,**kwargs):
        template_for_user=""
        if self.request.user.has_perm("auth.management_permission"):
            template_for_user="main\index_management.html"
            clientes_deudores=self.get_clientes_deudores()
            return {"template_for_user":template_for_user,"contratos":clientes_deudores}
        else:
            adeudo_mes=self.se_debe_el_mes(self.request.user.id)
            return {"template_for_user":"main\index_cliente.html",adeudo_mes:adeudo_mes}

    def get_clientes_deudores(self):
        ahora=datetime.today()
        ultimo_dia=calendar.monthrange(ahora.year,ahora.month)[1]
        fecha_final=datetime(ahora.year, ahora.month, ultimo_dia)  #year, month, day

        inicio_fecha=datetime.today().replace(day=1)
        clientes_si_pagaron=PagoCliente.objects.values_list("cliente__id",flat=True).filter(fecha_pago__range=[str(inicio_fecha),str(fecha_final)])
        return Contrato.objects.exclude(cliente__id__in=clientes_si_pagaron).filter(estado_contrato=True)

    def se_debe_el_mes(self,user_id):
        ahora=datetime.today()
        ultimo_dia=calendar.monthrange(ahora.year,ahora.month)[1]
        fecha_final=datetime(ahora.year, ahora.month, ultimo_dia)  #year, month, day
        inicio_fecha=datetime.today().replace(day=1)

        cliente_id=Cliente.objects.get(user_id=user_id).id
        return True#PagoCliente.objects.filter(fecha_pago__range=[str(inicio_fecha),str(fecha_final)],cliente_id=cliente_id).count()>0
