from django.contrib import admin
from .models import *


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre_entidad', 'tipo', 'parent',)
    list_filter = ('tipo',)


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('clave', 'cct', 'nombre', 'tipo', 'Localidad__nombre_entidad',)
    list_filter = ('tipo', 'enlace')


admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Escuela)
admin.site.register(ResultadoGlobal)
