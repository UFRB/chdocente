# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand

from ...models import Docente, Administrativo


class Command(BaseCommand):
    args = 'filename'
    help = 'Importa Docentes a partir de um arquivo JSON'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for item in data:
                try:
                    atividade = Administrativo(
                        docente=Docente.objects.get(matricula=item['matricula']),
                        semestre=item['semestre'],
                        afastamento=item['afastamento'],
                        cargo=item['cargo'],
                        )
                    atividade.save()
                    print("criada atividade para o docente %s" % item['matricula'])
                except Docente.DoesNotExist:
                    print('Docente %s não existe' % item['matricula'])