# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Disciplina


def RelatorioEnsino(request):
    # número de turmas por tipo
    turmas = Disciplina.objects.all()
    teoricas = turmas.filter(tipo='teorica')
    praticas = turmas.filter(tipo='pratica')
    estagio = turmas.filter(tipo='estagio')

    turmas_tipo = [
        ('Turmas Teóricas', teoricas.count()),
        ('Turmas Práticas', praticas.count()),
        ('Turmas de Estágio', estagio.count())
        ]

    turmas_multicampi = turmas.filter(multicampia=True).count()

    multicampia = [
        ('Turmas sem Multicampia', turmas.count() - turmas_multicampi),
        ('Turmas Multicampi', turmas_multicampi)
        ]

    turmas_nivel = [
        ('Turmas de Graduacao', turmas.filter(nivel='graduacao').count()),
        ('Turmas de Pós-Graduação', turmas.filter(nivel='pos').count())
        ]

    estudantes_turmas = [
            ['1-6', turmas.filter(estudantes__gte=1, estudantes__lte=6).count()],
            ['7-15', turmas.filter(estudantes__gte=7, estudantes__lte=15).count()],
            ['16-25', turmas.filter(estudantes__gte=16, estudantes__lte=25).count()],
            ['26-50', turmas.filter(estudantes__gte=26, estudantes__lte=50).count()],
            ['51-70', turmas.filter(estudantes__gte=51, estudantes__lte=70).count()],
            ['Mais que 70', turmas.filter(estudantes__gt=70).count()],
            ]

    estudantes_turmas_teoricas = [
            ['1-6', teoricas.filter(estudantes__gte=1, estudantes__lte=6).count()],
            ['7-15', teoricas.filter(estudantes__gte=7, estudantes__lte=15).count()],
            ['16-25', teoricas.filter(estudantes__gte=16, estudantes__lte=25).count()],
            ['26-50', teoricas.filter(estudantes__gte=26, estudantes__lte=50).count()],
            ['51-70', teoricas.filter(estudantes__gte=51, estudantes__lte=70).count()],
            ['Mais que 70', teoricas.filter(estudantes__gt=70).count()],
            ]

    estudantes_turmas_praticas = [
            ['1-6', praticas.filter(estudantes__gte=1, estudantes__lte=6).count()],
            ['7-15', praticas.filter(estudantes__gte=7, estudantes__lte=15).count()],
            ['16-25', praticas.filter(estudantes__gte=16, estudantes__lte=25).count()],
            ['26-50', praticas.filter(estudantes__gte=26, estudantes__lte=50).count()],
            ['51-70', praticas.filter(estudantes__gte=51, estudantes__lte=70).count()],
            ['Mais que 70', praticas.filter(estudantes__gt=70).count()],
            ]

    estudantes_turmas_estagio = [
            ['1-6', estagio.filter(estudantes__gte=1, estudantes__lte=6).count()],
            ['7-15', estagio.filter(estudantes__gte=7, estudantes__lte=15).count()],
            ['16-25', estagio.filter(estudantes__gte=16, estudantes__lte=25).count()],
            ['26-50', estagio.filter(estudantes__gte=26, estudantes__lte=50).count()],
            ['51-70', estagio.filter(estudantes__gte=51, estudantes__lte=70).count()],
            ['Mais que 70', estagio.filter(estudantes__gt=70).count()],
            ]

    return render(request, 'relatorio_ensino.html', {
        'turmas_tipo': turmas_tipo,
        'multicampia': multicampia,
        'turmas_nivel': turmas_nivel,
        'estudantes_turmas': estudantes_turmas,
        'estudantes_turmas_teoricas': estudantes_turmas_teoricas,
        'estudantes_turmas_praticas': estudantes_turmas_praticas,
        'estudantes_turmas_estagio': estudantes_turmas_estagio,
        })