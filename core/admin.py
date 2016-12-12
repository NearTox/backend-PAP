from django.contrib import admin
from .models import (DatosPostales, Cliente, Mensajero, Orden)
# Register your models here.

admin.site.register(DatosPostales)
admin.site.register(Cliente)
admin.site.register(Mensajero)
admin.site.register(Orden)
