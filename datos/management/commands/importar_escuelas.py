# -*- encoding: utf-8 -*-
from django.core.management.base import NoArgsCommand
from django.contrib.gis.geos import Point
import requests

from miescuela.datos.models import *

api_estado = "http://api.imco.org.mx/imco-compara-escuela/web_service.php?accion=datos.generales.escuela.x.estado&id_entidad=21"
api_resultados = 'http://api.imco.org.mx/imco-compara-escuela/web_service.php?accion=datos.resultados.examenes.x.escuela.todos.anios&id_escuela=%s&anio=2007&modalidad=calificaciones'


class Command(NoArgsCommand):
    help = "Importa escuelas"

    def handle_noargs(self, **options):
        estado = requests.get(api_estado)
        estado = estado.json()
        municipios_dict = estado['municipios']
        datos_estado = estado['datos_estado'][0]
        edo = Localidad(clave=21,
                        nombre_entidad=datos_estado['nombre_entidad'],
                        tipo=datos_estado['tipo'])
        edo.save()
        cuenta_municipios = 0
        cuenta_escuelas = 0
        for municipio in municipios_dict:
            print "Creando municipio", municipio
            mpio_dict = municipios_dict[municipio]['datos_municipio'][0]
            mpio = Localidad(clave=int(municipio),
                             nombre_entidad=mpio_dict['nombre_entidad'],
                             tipo=mpio_dict['tipo'],
                             parent=edo)
            mpio.save()
            mpio_loc_dict = municipios_dict[municipio]['localidades']
            for localidad in mpio_loc_dict:
                print "Creando localidad", localidad
                local_dict = mpio_loc_dict[localidad]['datos_localidad'][0]
                local = Localidad(clave=local_dict['id'],
                                  nombre_entidad=local_dict['nombre_entidad'],
                                  tipo=local_dict['tipo'],
                                  parent=mpio)
                local.save()
                local_escuelas_dict = mpio_loc_dict[localidad]['datos_escuelas']
                for escuela in local_escuelas_dict:
                    print "Creando la escuela", escuela
                    escuela_dict = local_escuelas_dict[escuela]
                    clave = escuela_dict['clave'] = escuela_dict['id']
                    del escuela_dict['id']
                    escuela_dict['localidad'] = local
                    escuela_dict['altitud'] = int(escuela_dict['altitud'])
                    # Convirtiendo a punto geolocalizable
                    escuela_dict['point'] = Point(float(escuela_dict['longitud']), float(escuela_dict['latitud']))
                    del escuela_dict['longitud']
                    del escuela_dict['latitud']
                    esc = Escuela(**escuela_dict)
                    esc.save()
                    resultados = requests.get(api_resultados % clave)
                    resultados = resultados.json()
                    res = resultados['resultados']
                    tiene_enlace = 0
                    for periodo in res:
                        print "Insertando periodo ", periodo
                        estadisticas = res[periodo]['global']['estadisticas']
                        estadisticas['escuela'] = esc
                        estadisticas['periodo'] = int(periodo)
                        resultados = ResultadoGlobal(**estadisticas)
                        resultados.save()
                        tiene_enlace += 1

                    # Si ha realizado prueba enlace
                    if tiene_enlace:
                        esc.enlace = True

                    # Extrayendo tipo de escuela
                    if esc.cct.startswith('21PE'):
                        esc.tipo = 'secundaria'
                    elif esc.cct.startswith('21PP'):
                        esc.tipo = 'primaria'
                    elif esc.cct.startswith('21PJ'):
                        esc.tipo = 'jardin'
                    elif esc.cct.startswith('21BB'):
                        esc.tipo = 'biblioteca'
                    else:
                        esc.tipo = 'otro'

                    esc.save()
                    cuenta_escuelas += 1
                    print
                    print "escuela # ", cuenta_escuelas
                    print

            cuenta_municipios += 1
            print
            print "municipio # ", cuenta_municipios
            print
