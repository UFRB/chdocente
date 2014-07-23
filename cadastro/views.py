# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Max, Min


from .models import Disciplina


def RelatorioEnsino(request):
    # número de turmas por tipo
    turmas = Disciplina.objects.all()

    turmas_tipo = [
        ('Turmas Teóricas', turmas.filter(tipo='teorica').count()),
        ('Turmas Práticas', turmas.filter(tipo='pratica').count()),
        ('Turmas de Estágio', turmas.filter(tipo='estagio').count())
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
            ['1-5', turmas.filter(estudantes__gte=1, estudantes__lte=5).count()],
            ['6-10', turmas.filter(estudantes__gte=6, estudantes__lte=10).count()],
            ['11-20', turmas.filter(estudantes__gte=11, estudantes__lte=20).count()],
            ['21-30', turmas.filter(estudantes__gte=21, estudantes__lte=30).count()],
            ['31-40', turmas.filter(estudantes__gte=31, estudantes__lte=40).count()],
            ['Mais que 40', turmas.filter(estudantes__gte=41).count()],
            ]

    return render(request, 'relatorio_ensino.html', {
        'turmas_tipo': turmas_tipo,
        'multicampia': multicampia,
        'turmas_nivel': turmas_nivel,
        'estudantes_turmas': estudantes_turmas
        })