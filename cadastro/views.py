# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Disciplina, Docente, Pesquisa, Extensao, Administrativo


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
        centro = request.GET['centro']
        turmas = Disciplina.objects.filter(docente__centro=centro)
    else:
        centro = ''
        turmas = Disciplina.objects.all()

    if 'semestre' in request.GET and request.GET['semestre']:
        semestre = request.GET['semestre']
        turmas = turmas.filter(semestre=semestre)
    else:
        semestre = ''

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
        'centro': centro,
        'semestre': semestre,
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
        centro = request.GET['centro']
        docentes_ensino = Disciplina.objects.filter(docente__centro=centro)
        docentes_pesquisa = Pesquisa.objects.filter(docente__centro=centro)
        docentes_extensao = Extensao.objects.filter(docente__centro=centro)
        docentes_admin = Administrativo.objects.filter(docente__centro=centro)
        num_docentes = Docente.objects.filter(centro=centro).count()
    else:
        centro = ''
        docentes_ensino = Disciplina.objects.all()
        docentes_pesquisa = Pesquisa.objects.all()
        docentes_extensao = Extensao.objects.all()
        docentes_admin = Administrativo.objects.all()
        num_docentes = Docente.objects.all().count()

    if 'semestre' in request.GET and request.GET['semestre']:
        semestre = request.GET['semestre']
        docentes_ensino = docentes_ensino.filter(semestre=semestre)
        docentes_pesquisa = docentes_pesquisa.filter(semestre=semestre)
        docentes_extensao = docentes_extensao.filter(semestre=semestre)
        docentes_admin = docentes_admin.filter(semestre=semestre)
    else:
        semestre = ''

    docentes_ensino = [disciplina.docente
        for disciplina in docentes_ensino.distinct('docente')]
    docentes_pesquisa = [projeto.docente
        for projeto in docentes_pesquisa.distinct('docente')]
    docentes_extensao = [projeto.docente
        for projeto in docentes_extensao.distinct('docente')]

    docentes_ens_pes = [docente for docente in docentes_pesquisa
        if docente in docentes_ensino]
    docentes_ens_ext = [docente for docente in docentes_extensao
        if docente in docentes_ensino]
    docentes_ens_pes_ext = [docente for docente in docentes_ens_pes
        if docente in docentes_ens_ext]

    num_docentes_ensino = len(docentes_ensino)
    num_docentes_pesquisa = len(docentes_pesquisa)
    num_docentes_extensao = len(docentes_extensao)
    num_docentes_afastados = docentes_admin.filter(afastamento=True) \
        .distinct('docente').count()
    docentes_admin = docentes_admin \
        .filter(cargo__in=['fg', 'cd', 'fuc'])

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

    ens_pes_ext = [
        ['Sim', len(docentes_ens_pes_ext)],
        ['Não', num_docentes - len(docentes_ens_pes_ext)]
        ]

    ens_pes = [
        ['Sim', len(docentes_ens_pes)],
        ['Não', num_docentes - len(docentes_ens_pes)]
        ]

    ens_ext = [
        ['Sim', len(docentes_ens_ext)],
        ['Não', num_docentes - len(docentes_ens_ext)]
        ]

    administrativo = [
        ['Com atividades administrativas', docentes_admin
            .distinct('docente').count()],
        ['Sem atividades administrativas', num_docentes - docentes_admin
            .distinct('docente').count()]
        ]

    admin_detalhes = [
        ['FG', docentes_admin.filter(cargo='fg').distinct('docente').count()],
        ['CD', docentes_admin.filter(cargo='cd').distinct('docente').count()],
        ['Coordenação de Colegiado', docentes_admin.filter(cargo='fuc')
            .distinct('docente').count()],
        ]

    afastamento = [
        ['Docentes afastados', num_docentes_afastados],
        ['Docentes em exercício', num_docentes - num_docentes_afastados]
        ]

    return render(request, 'relatorio_docente.html', {
        'centro': centro,
        'semestre': semestre,
        'ensino': ensino,
        'ens_pes_ext': ens_pes_ext,
        'ens_pes': ens_pes,
        'ens_ext': ens_ext,
        'pesquisa': pesquisa,
        'extensao': extensao,
        'administrativo': administrativo,
        'admin_detalhes': admin_detalhes,
        'afastamento': afastamento
        })
