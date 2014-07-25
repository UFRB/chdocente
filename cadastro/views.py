# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Count

from .models import Disciplina, Docente, Pesquisa, Extensao


def query_estudantes(query):
    result = [
            ['1-6', query.filter(estudantes__gte=1, estudantes__lte=6).count()],
            ['7-15', query.filter(estudantes__gte=7, estudantes__lte=15).count()],
            ['16-25', query.filter(estudantes__gte=16, estudantes__lte=25).count()],
            ['26-50', query.filter(estudantes__gte=26, estudantes__lte=50).count()],
            ['51-70', query.filter(estudantes__gte=51, estudantes__lte=70).count()],
            ['Mais que 70', query.filter(estudantes__gt=70).count()],
            ]
    return result


def RelatorioEnsino(request):
    if 'centro' in request.GET and request.GET['centro']:
        turmas = Disciplina.objects.filter(docente__centro=request.GET['centro'])
    else:
        turmas = Disciplina.objects.all()

    if 'semestre' in request.GET and request.GET['semestre']:
        turmas = turmas.filter(semestre=request.GET['semestre'])

    # número de turmas por tipo
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

    estudantes_turmas = query_estudantes(turmas)

    estudantes_turmas_teoricas = query_estudantes(teoricas)

    estudantes_turmas_praticas = query_estudantes(praticas)

    estudantes_turmas_estagio = query_estudantes(estagio)

    return render(request, 'relatorio_ensino.html', {
        'turmas_tipo': turmas_tipo,
        'multicampia': multicampia,
        'turmas_nivel': turmas_nivel,
        'estudantes_turmas': estudantes_turmas,
        'estudantes_turmas_teoricas': estudantes_turmas_teoricas,
        'estudantes_turmas_praticas': estudantes_turmas_praticas,
        'estudantes_turmas_estagio': estudantes_turmas_estagio,
        })


def RelatorioDocente(request):

    if 'centro' in request.GET and request.GET['centro']:
        num_docentes_ensino = Disciplina.objects.filter(docente__centro=request.GET['centro'])
        num_docentes_pesquisa = Pesquisa.objects.filter(docente__centro=request.GET['centro'])
        num_docentes_extensao = Extensao.objects.filter(docente__centro=request.GET['centro'])
    else:
        num_docentes_ensino = Disciplina.objects.all()
        num_docentes_pesquisa = Pesquisa.objects.all()
        num_docentes_extensao = Extensao.objects.all()

    if 'semestre' in request.GET and request.GET['semestre']:
        num_docentes_ensino = num_docentes_ensino.filter(semestre=request.GET['semestre'])
        num_docentes_pesquisa = num_docentes_pesquisa.filter(semestre=request.GET['semestre'])
        num_docentes_extensao = num_docentes_extensao.filter(semestre=request.GET['semestre'])

    num_docentes_ensino = num_docentes_ensino.distinct('docente').count()
    num_docentes_pesquisa = num_docentes_pesquisa.distinct('docente').count()
    num_docentes_extensao = num_docentes_extensao.distinct('docente').count()

    num_docentes = Docente.objects.all().count()

    ensino = [
        ['Com atividades de ensino', num_docentes_ensino],
        ['Sem atividades de ensino', num_docentes - num_docentes_ensino]
        ]

    pesquisa = [
        ['Com atividades de pesquisa', num_docentes_pesquisa],
        ['Sem atividades de pesquisa', num_docentes - num_docentes_pesquisa]
        ]

    extensao = [
        ['Com atividades de extensão', num_docentes_extensao],
        ['Sem atividades de extensão', num_docentes - num_docentes_extensao]
        ]

    return render(request, 'relatorio_docente.html', {
        'ensino': ensino,
        'pesquisa': pesquisa,
        'extensao': extensao
        })