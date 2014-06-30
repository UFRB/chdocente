# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand

from ...models import Docente, Disciplina


class Command(BaseCommand):
    args = 'filename'
    help = 'Importa Docentes a partir de um arquivo JSON'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for item in data:
                try:
                    disciplina = Disciplina(
                        docente=Docente.objects.get(nome=item['docente']),
                        semestre=item['semestre'],
                        codigo=item['codigo'],
                        nome=item['nome'],
                        cargahoraria=item['cargahoraria'],
                        tipo=item['tipo'],
                        nivel=item['nivel'],
                        estudantes=item['estudantes']
                        )
                    disciplina.save()
                except Docente.DoesNotExist:
                    print('Docente %s não existe' % item['docente'])