from django.contrib import admin
from .models import *


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre_entidad', 'tipo', 'parent',)
    list_filter = ('tipo',)


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('clave', 'cct', 'nombre', 'tipo', 'localidad',)
    list_filter = ('tipo', 'enlace', 'valida')


admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(ResultadoGlobal)
