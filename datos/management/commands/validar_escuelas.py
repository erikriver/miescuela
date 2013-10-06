import csv
from django.core.management.base import NoArgsCommand
from miescuela.datos.models import *


file_csv = "data/escuela_valida.csv"


class Command(NoArgsCommand):
    help = "Validar escuelas"

    def handle_noargs(self, **options):
        with open(file_csv, 'rb') as csvfile:
            validas = csv.reader(csvfile)  # , delimiter=',', quotechar='"')
            no_existe = []
            for row in validas:
                try:
                    escuela = Escuela.objects.get(cct=row[1].strip())
                    escuela.valida = True
                    inicio = row[2].strip().split()
                    escuela.mes_inicio = inicio[0]
                    escuela.anio_inicio = int(inicio[1])
                    escuela.save()
                    print escuela.nombre
                except:
                    no_existe.append(row[1].strip())
                    print "No existe la escuela", row[1].strip()

        with open('data/no_existen.csv', 'wb') as f:
            writer = csv.writer(f)
            for r in no_existe:
                writer.writerow(r)
