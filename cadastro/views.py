from django.shortcuts import render
from .models import Disciplina


def relatorio(request, centro):
    disciplinas = Disciplina.objects.filter(docente__centro=centro) \
        .order_by('docente')

    return render(request, 'relatorio.html',
        {'centro': centro, 'disciplinas': disciplinas})