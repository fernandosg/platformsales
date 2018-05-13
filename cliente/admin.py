from django.contrib import admin

from cliente.models import (Cliente, PagoCliente)
from departamento.models import Departamento
from edificio.models import Edificio 
from contratos.models import Contrato
from puntoenlace.models import PuntoEnlace
from reportes.models import MensajeOperacion

admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(PagoCliente)
admin.site.register(Contrato)
admin.site.register(PuntoEnlace)
admin.site.register(MensajeOperacion)
admin.site.register(Edificio)
