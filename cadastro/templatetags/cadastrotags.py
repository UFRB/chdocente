# -*- coding: utf-8 -*-
from django import template

from ..models import Docente, Administrativo

register = template.Library()

@register.inclusion_tag('tags/dados_docente.html')
def carga_horaria(docente, semestre):
    docente = Docente.objects.get(nome=docente)

    ch_ensino = docente.ch_ensino(semestre) / 6
    ch_pesquisa = docente.ch_pesquisa(semestre)
    ch_extensao = docente.ch_extensao(semestre)
    ch_total = ch_ensino + ch_pesquisa + ch_extensao
    try:
        cargo = docente.administrativo_set.get(semestre=semestre).get_cargo_display()
        afastamento = docente.administrativo_set.get(semestre=semestre).afastamento
    except Administrativo.DoesNotExist:
        cargo= ''
        afastamento = 'False'

    return {
        'docente': docente,
        'ch_ensino': ch_ensino,
        'ch_pesquisa': ch_pesquisa,
        'ch_extensao': ch_extensao,
        'ch_total': ch_total,
        'cargo': cargo,
        'afastamento': afastamento,
        }