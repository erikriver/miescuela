from tastypie.resources import ModelResource
from tastypie import fields
from django.db.models import Q
from .models import *


class ResultadoGlobalResource(ModelResource):
    """docstring for ResultadoGlobal"""

    class Meta:
        queryset = ResultadoGlobal.objects.all()
        resource_name = 'resultadoglobal'
        excludes = ['id', 'desv_std_esp', 'desv_std_mat', 'desv_std_extra']
        include_resource_uri = False
        include_absolute_url = False


class EscuelaResource(ModelResource):
    """docstring for EscuelaResource"""
    resultados = fields.ToManyField(ResultadoGlobalResource, 'resultadoglobal_set', full=True, null=True)

    class Meta:
        queryset = Escuela.objects.all()
        resource_name = 'escuela'
        fields = ['id', 'title']
        include_resource_uri = False
        include_absolute_url = False


class LocalidadResource(ModelResource):
    """docstring for LocalidadResource"""
    escuelas = fields.ToManyField(EscuelaResource, 'escuela_set', full=True, null=True)

    class Meta:
        queryset = Localidad.objects.all()
        resource_name = 'localidad'
        fields = ['id', 'title']
        include_resource_uri = False
        include_absolute_url = False
