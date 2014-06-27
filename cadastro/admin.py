# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Docente, Administrativo, Disciplina, Extensao, Pesquisa


class AdminSite(admin.ModelAdmin):

    site_header = "Carga Horária Docente"

class DisciplinaAdmin(admin.ModelAdmin):

    list_display = ('codigo', 'nome', 'semestre', 'docente')
    list_filter = ('semestre', 'docente__centro')
    search_fields = ('codigo', 'nome', 'docente__nome', 'docente__matricula')

    def get_queryset(self, request):
        qs = super(DisciplinaAdmin, self).get_queryset(request)
        groups = [group.name for group in request.user.groups.all()]
        if request.user.is_superuser:
            return qs
        return qs.filter(docente__centro__in=groups)


class PesquisaAdmin(admin.ModelAdmin):

    list_display = ('semestre', 'docente', 'area', 'financiador')
    list_filter = ('semestre', 'docente__centro', 'area', 'financiador')
    search_fields = ('docente__nome', 'docente__matricula')
    ordering = ['docente__nome']

    def get_queryset(self, request):
        qs = super(PesquisaAdmin, self).get_queryset(request)
        groups = [group.name for group in request.user.groups.all()]
        if request.user.is_superuser:
            return qs
        return qs.filter(docente__centro__in=groups)


class ExtensaoAdmin(admin.ModelAdmin):

    list_display = ('semestre', 'docente', 'area', 'financiador')
    list_filter = ('semestre', 'docente__centro', 'area', 'financiador')
    search_fields = ('docente__nome', 'docente__matricula')
    ordering = ['docente__nome']

    def get_queryset(self, request):
        qs = super(ExtensaoAdmin, self).get_queryset(request)
        groups = [group.name for group in request.user.groups.all()]
        if request.user.is_superuser:
            return qs
        return qs.filter(docente__centro__in=groups)


class AdministrativoAdmin(admin.ModelAdmin):

    list_filter = ('semestre', 'docente__centro', 'cargo', 'comissoes')
    list_display = ('docente', 'semestre', 'cargo', 'comissoes')
    ordering = ['docente__nome']

    def get_queryset(self, request):
        qs = super(AdministrativoAdmin, self).get_queryset(request)
        groups = [group.name for group in request.user.groups.all()]
        if request.user.is_superuser:
            return qs
        return qs.filter(docente__centro__in=groups)


class DocenteAdmin(admin.ModelAdmin):

    search_fields = ['nome', 'matricula']
    list_filter = ('centro',)
    list_display = ('nome', 'matricula', 'centro')
    ordering = ['nome']

    def get_queryset(self, request):
        qs = super(DocenteAdmin, self).get_queryset(request)
        groups = [group.name for group in request.user.groups.all()]
        if request.user.is_superuser:
            return qs
        return qs.filter(docente__centro__in=groups)


admin.site.register(Docente, DocenteAdmin)
admin.site.register(Administrativo, AdministrativoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Pesquisa, PesquisaAdmin)
admin.site.register(Extensao, ExtensaoAdmin)
