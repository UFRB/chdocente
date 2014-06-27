# -*- coding: utf-8 -*-

from django.db import models


class Docente(models.Model):

    CENTROS = (
        ('cahl', 'CAHL'),
        ('ccaab', 'CCAAB'),
        ('ccs', 'CCS'),
        ('cetec', 'CETEC'),
        ('cfp', 'CFP')
        )

    matricula = models.CharField(max_length=7, unique=True)
    nome = models.CharField(max_length=100, unique=True)
    centro = models.CharField(choices=CENTROS, max_length=11)

    def __str__(self):
        return '%s - %s' % (self.matricula, self.nome)


class Disciplina(models.Model):

    NIVEIS = (
        ('graduacao', 'Graduação'),
        ('pos', 'Pós-Graduação')
        )

    TIPOS = (
        ('teorica', 'Teórica'),
        ('pratica', 'Prática'),
        ('estagio', 'Estágio')
        )

    SEMESTRES = (
        ('20131', '2013.1'),
        ('20132', '2013.2')
        )

    docente = models.ForeignKey(Docente)
    semestre = models.CharField(choices=SEMESTRES, max_length=6)
    codigo = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    nivel = models.CharField('Nível', choices=NIVEIS, max_length=11)
    multicampia = models.BooleanField(default=False)
    tipo = models.CharField(choices=TIPOS, max_length=11)
    cargahoraria = models.IntegerField('Carga horária', max_length=3)
    estudantes = models.IntegerField('Número de Estudantes', max_length=3)

    def __str__(self):
        return '%s' % (self.codigo)


class Pesquisa(models.Model):

    AREAS_PESQUISA = (
        ('exatas', 'Ciências Exatas e da Terra'),
        ('biologicas', 'Ciências Biológicas'),
        ('saude', 'Ciências da Saúde'),
        ('agrarias', 'Ciências Agrárias'),
        ('sociais', 'Ciências Sociais Aplicadas'),
        ('humanas', 'Ciências Humanas'),
        ('engenharias', 'Engenharias'),
        ('linguistica', 'Linguística, Letras e Artes'),
        ('outros', 'Outros')
        )

    FINANCIADORES = (
        ('semfinanciamento', 'Sem financiamento'),
        ('bndes', 'BNDES'),
        ('petrobras', 'Petrobras'),
        ('eletrobras', 'Eletrobras'),
        ('bnb', 'Banco do Nordeste'),
        ('natura', 'Natura'),
        ('cnpq', 'CNPq'),
        ('mcti', 'MCTI'),
        ('outros', 'Outros')
        )

    SEMESTRES = (
        ('20131', '2013.1'),
        ('20132', '2013.2')
        )

    docente = models.ForeignKey(Docente)
    semestre = models.CharField(choices=SEMESTRES, max_length=6)
    area = models.CharField(choices=AREAS_PESQUISA, max_length=20)
    financiador = models.CharField(choices=FINANCIADORES, max_length=20)
    estudantes_graduacao = models.IntegerField('Número de Estudantes de Graduação', max_length=2, null=True, blank=True)
    estudantes_pos = models.IntegerField('Número de Estudantes de Pós-Graduação', max_length=2, null=True, blank=True)
    bolsistas_pibic = models.IntegerField('Número de Bolsistas PIBIC/PIBITI', max_length=2, null=True, blank=True)
    bolsistas_ppq = models.IntegerField('Número de Bolsistas PPQ', max_length=2, null=True, blank=True)
    voluntarios = models.IntegerField('Número de Voluntários', max_length=2, null=True, blank=True)
    parceria = models.CharField('Parceria Institucional', max_length=255, blank=True)
    parceria_inter = models.CharField('Parceria Interinstitucional', max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)

    class Meta:
        verbose_name = 'Projeto de Pesquisa'
        verbose_name_plural = 'Projetos de Pesquisa'


class Extensao(models.Model):

    AREAS_EXTENSAO = (
    ('comunicacao', 'Comunicação'),
    ('cultura', 'Cultura'),
    ('direitoshumanos', 'Direitos Humanos e Justiça'),
    ('educacao', 'Educação'),
    ('meioambiente', 'Meio Ambiente'),
    ('saude', 'Saúde'),
    ('tecnologia', 'Tecnologia e Produção'),
    ('trabalho', 'Trabalho')
    )

    FINANCIADORES_EXTENSAO = (
        ('pibex', 'PIBEX'),
        ('proext', 'PROEXT-MEC-SESU')
        )

    SEMESTRES = (
        ('20131', '2013.1'),
        ('20132', '2013.2')
        )

    docente = models.ForeignKey(Docente)
    semestre = models.CharField(choices=SEMESTRES, max_length=6)
    area = models.CharField(choices=AREAS_EXTENSAO, max_length=20)
    financiador = models.CharField(choices=FINANCIADORES_EXTENSAO, max_length=20)
    estudantes_graduacao = models.IntegerField('Número de Estudantes de Graduação', max_length=2, null=True, blank=True)
    estudantes_pos = models.IntegerField('Número de Estudantes de Pós-Graduação', max_length=2, null=True, blank=True)
    bolsistas_pibex = models.IntegerField('Número de Bolsistas PIBEX', max_length=2, null=True, blank=True)
    bolsistas_ppq = models.IntegerField('Número de Bolsistas PPQ', max_length=2, null=True, blank=True)
    voluntarios = models.IntegerField('Número de Voluntários', max_length=2, null=True, blank=True)
    parceria = models.CharField('Parceria Institucional', max_length=255, blank=True)
    parceria_inter = models.CharField('Parceria Interinstitucional', max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)

    class Meta:
        verbose_name = 'Projeto de Extensão'
        verbose_name_plural = 'Projetos de Extensão'


class Administrativo(models.Model):

    CARGOS = (
        ('fg', 'FG - Função Gratificada'),
        ('cd', 'CD - Cargo de Direção'),
        ('fuc', 'Coordenador de Colegiado'),
        )

    SEMESTRES = (
        ('20131', '2013.1'),
        ('20132', '2013.2')
        )

    docente = models.ForeignKey(Docente)
    semestre = models.CharField(choices=SEMESTRES, max_length=6)
    afastamento = models.BooleanField(default=False)
    cargo = models.CharField(choices=CARGOS, max_length=100, blank=True)
    comissoes = models.IntegerField('Número de comissões', max_length=2, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.docente, self.semestre)

    class Meta:
        verbose_name = 'Atividade Administrativa'
        verbose_name_plural = 'Atividades Administrativas'