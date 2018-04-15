from django.contrib import admin

from cliente.models import (Cliente, Departamento, PagoCliente)
from contratos.models import Contrato
from puntoenlace.models import PuntoEnlace
from reportes.models import MensajeOperacion

admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(PagoCliente)
admin.site.register(Contrato)
admin.site.register(PuntoEnlace)
admin.site.register(MensajeOperacion)
