from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Disciplina


@login_required(login_url='/admin/')
def relatorio(request, centro):
    disciplinas = Disciplina.objects.filter(docente__centro=centro) \
        .order_by('docente')

    return render(request, 'relatorio.html',
        {'centro': centro, 'disciplinas': disciplinas})