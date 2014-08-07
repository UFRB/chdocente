# -*- coding: utf-8 -*-
import unicodecsv
from collections import Counter

from django.http import HttpResponse
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


def filtro_por_centro(data):
    result = [
        ['CAHL', data.filter(docente__centro='cahl').count()],
        ['CCAAB', data.filter(docente__centro='ccaab').count()],
        ['CCS', data.filter(docente__centro='ccs').count()],
        ['CETEC', data.filter(docente__centro='cetec').count()],
        ['CFP', data.filter(docente__centro='cfp').count()],
        ]
    return result


def RelatorioProjetos(request):

    return render(request, 'relatorio_projetos.html', {
        'pesquisa': filtro_por_centro(Pesquisa.objects.all()),
        'extensao': filtro_por_centro(Extensao.objects.all()),
        'pesquisa_20131': filtro_por_centro(Pesquisa.sem_20131.all()),
        'pesquisa_20132': filtro_por_centro(Pesquisa.sem_20132.all()),
        'extensao_20131': filtro_por_centro(Extensao.sem_20131.all()),
        'extensao_20132': filtro_por_centro(Extensao.sem_20132.all()),
        })


def valores_ch(data):
    result = [
        ['Menos que 10', sum([item[1] for item in data.items() if item[0]<170])],
        ['10h', sum([item[1] for item in data.items() if item[0]>=170 and item[0]<187])],
        ['11h', sum([item[1] for item in data.items() if item[0]>=187 and item[0]<204])],
        ['12h', sum([item[1] for item in data.items() if item[0]>=204 and item[0]<221])],
        ['13h', sum([item[1] for item in data.items() if item[0]>=221 and item[0]<238])],
        ['14h', sum([item[1] for item in data.items() if item[0]>=238 and item[0]<255])],
        ['15h', sum([item[1] for item in data.items() if item[0]>=255 and item[0]<272])],
        ['16h', sum([item[1] for item in data.items() if item[0]>=272 and item[0]<289])],
        ['Mais que 16h', sum([item[1] for item in data.items() if item[0]>289])],
        ]

    return result


def RelatorioCargaHoraria(request):

    if 'centro' in request.GET and request.GET['centro']:
        centro = request.GET['centro']
        docentes = Docente.objects.filter(centro=centro)
    else:
        centro = ''
        docentes = Docente.objects.all()

    ensino_20131 = valores_ch(Counter([i.ch_ensino('20131') for i in docentes]))
    ensino_20132 = valores_ch(Counter([i.ch_ensino('20132') for i in docentes]))

    return render(request, 'relatorio_ch.html', {
        'centro': centro,
        'ensino_20131': ensino_20131,
        'ensino_20132': ensino_20132,
        })


def RelatorioGeral(request):

    if 'centro' in request.GET and request.GET['centro']:
        centro = request.GET['centro']
        docentes = Docente.objects.filter(centro=centro)
    else:
        centro = ''
        docentes = Docente.objects.all()

    if 'semestre' in request.GET and request.GET['semestre']:
        semestre = request.GET['semestre']
    else:
        semestre = '20131'

    return render(request, 'relatorio_geral.html',{
        'docentes': docentes,
        'centro': centro,
        'semestre': semestre
        })


def ExportarDisciplina(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="disciplinas.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow(['Centro', 'Código', 'Nome', 'Docente', 'Semestre', 'Tipo',
        'Nível', 'Multicampia', 'Carga horária', 'Estudantes'])

    for disciplina in Disciplina.objects.all():
        writer.writerow([disciplina.docente.centro, disciplina.codigo,
             disciplina.nome, disciplina.docente, disciplina.semestre,
             disciplina.tipo, disciplina.nivel, disciplina.multicampia,
             disciplina.cargahoraria, disciplina.estudantes])

    return response


def ExportarPesquisa(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pesquisa.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow(['Centro', 'Nome', 'Docente', 'Semestre', 'Área',
        'Financiador', 'Carga horária', 'Estudantes de Graduação',
        'Estudantes de Pós', 'Bolsistas PIBIC/PIBITI', 'Bolsistas PPQ',
        'Voluntários', 'Parceria Institucional', 'Parceria Interinstitucional'])

    for projeto in Pesquisa.objects.all():
        writer.writerow([projeto.docente.centro, projeto.nome, projeto.docente,
             projeto.semestre, projeto.area, projeto.financiador,
             projeto.cargahoraria, projeto.estudantes_graduacao,
             projeto.estudantes_pos, projeto.bolsistas_pibic,
             projeto.bolsistas_ppq, projeto.voluntarios, projeto.parceria,
             projeto.parceria_inter])

    return response


def ExportarExtensao(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="extensao.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow(['Centro', 'Nome', 'Docente', 'Semestre', 'Área',
        'Financiador', 'Carga horária', 'Estudantes de Graduação',
        'Estudantes de Pós', 'Bolsistas PIBEX', 'Bolsistas PPQ',
        'Voluntários', 'Parceria Institucional', 'Parceria Interinstitucional'])

    for projeto in Extensao.objects.all():
        writer.writerow([projeto.docente.centro, projeto.nome, projeto.docente,
             projeto.semestre, projeto.area, projeto.financiador,
             projeto.cargahoraria, projeto.estudantes_graduacao,
             projeto.estudantes_pos, projeto.bolsistas_pibex,
             projeto.bolsistas_ppq, projeto.voluntarios, projeto.parceria,
             projeto.parceria_inter])

    return response


def ExportarAdministrativo(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="administrativo.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow(['Centro', 'Docente', 'Semestre', 'Afastamento', 'Cargo',
        'Comissões'])

    for atividade in Administrativo.objects.all():
        writer.writerow([atividade.docente.centro, atividade.docente,
            atividade.semestre, atividade.afastamento, atividade.cargo,
            atividade.comissoes])

    return response
