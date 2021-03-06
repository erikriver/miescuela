from django.contrib.gis.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Localidad(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    clave = models.IntegerField(blank=True, null=True)
    nombre_entidad = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)  # estado, municipio, localidad

    class Meta:
        verbose_name = 'localidad'
        verbose_name_plural = 'Localidades'

    def __unicode__(self):
        return self.nombre_entidad


class Escuela(models.Model):
    localidad = models.ForeignKey(Localidad)
    clave = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cct = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=255, blank=True, null=True)
    correo_electronico = models.CharField(max_length=255, blank=True, null=True)
    domicilio = models.TextField(blank=True, null=True)
    entre_calle_1 = models.TextField(blank=True, null=True)
    entre_calle_2 = models.TextField(blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    fax_extension = models.CharField(max_length=255, blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    point = models.PointField(srid=4326)
    pagina_web = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    telextension = models.CharField(max_length=255, blank=True, null=True)
    valida = models.BooleanField(default=False)
    enlace = models.BooleanField(default=False)
    tipo = models.CharField(max_length=50, blank=True, null=True)  # Jardin, Primaria, Secundaria
    mes_inicio = models.CharField(max_length=255, blank=True, null=True)
    anio_inicio = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'

    def __unicode__(self):
        return self.nombre


class ResultadoGlobal(models.Model):
    escuela = models.ForeignKey(Escuela)
    periodo = models.IntegerField(blank=True, null=True)
    promedio_esp = models.FloatField(blank=True, null=True)
    promedio_mat = models.FloatField(blank=True, null=True)
    promedio_extra = models.FloatField(blank=True, null=True)
    desv_std_esp = models.FloatField(blank=True, null=True)
    desv_std_mat = models.FloatField(blank=True, null=True)
    desv_std_extra = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Resultado Global'
        verbose_name_plural = 'Resultados Globales'

    def __unicode__(self):
        return "%s - %s" % (self.escuela, self.periodo)
