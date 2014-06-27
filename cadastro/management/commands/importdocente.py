# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand

from ...models import Docente


class Command(BaseCommand):
    args = 'filename'
    help = 'Importa Docentes a partir de um arquivo JSON'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for item in data:
                try:
                    docente = Docente.objects.get(matricula=item['matricula'])
                    if docente.nome != item['nome']:
                        docente.nome = item['nome']
                        docente.save()
                        print(("%s atualizado" % docente))
                except Docente.DoesNotExist:
                    docente = Docente(nome=item['nome'],
                                        matricula=item['matricula'],
                                        centro=item['centro']
                                    )
                    docente.save()
                    print(("%s criado" % docente))