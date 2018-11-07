from django.contrib import admin
from m2m.models import Marca, Cliente, Carro, CarroAdmin, Venta, VentaAdmin

admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(CarroAdmin)
admin.site.register(VentaAdmin)
