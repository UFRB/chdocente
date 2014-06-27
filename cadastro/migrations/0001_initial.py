# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Docente'
        db.create_table('cadastro_docente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=7, unique=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('cadastro', ['Docente'])

        # Adding model 'Disciplina'
        db.create_table('cadastro_disciplina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('multicampia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('cargahoraria', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('estudantes', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('cadastro', ['Disciplina'])

        # Adding model 'Pesquisa'
        db.create_table('cadastro_pesquisa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('financiador', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('estudantes_pos', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('bolsistas_pibic', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('voluntarios', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('parceria', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('parceria_inter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('cadastro', ['Pesquisa'])

        # Adding model 'Extensao'
        db.create_table('cadastro_extensao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('financiador', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('estudantes_pos', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('bolsistas_pibex', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('voluntarios', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('parceria', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('parceria_inter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('cadastro', ['Extensao'])

        # Adding model 'Atividade'
        db.create_table('cadastro_atividade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'])),
            ('afastamento', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('comissoes', self.gf('django.db.models.fields.IntegerField')()),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('cadastro', ['Atividade'])

        # Adding M2M table for field disciplinas on 'Atividade'
        m2m_table_name = db.shorten_name('cadastro_atividade_disciplinas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('atividade', models.ForeignKey(orm['cadastro.atividade'], null=False)),
            ('disciplina', models.ForeignKey(orm['cadastro.disciplina'], null=False))
        ))
        db.create_unique(m2m_table_name, ['atividade_id', 'disciplina_id'])

        # Adding M2M table for field pesquisa on 'Atividade'
        m2m_table_name = db.shorten_name('cadastro_atividade_pesquisa')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('atividade', models.ForeignKey(orm['cadastro.atividade'], null=False)),
            ('pesquisa', models.ForeignKey(orm['cadastro.pesquisa'], null=False))
        ))
        db.create_unique(m2m_table_name, ['atividade_id', 'pesquisa_id'])

        # Adding M2M table for field extensao on 'Atividade'
        m2m_table_name = db.shorten_name('cadastro_atividade_extensao')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('atividade', models.ForeignKey(orm['cadastro.atividade'], null=False)),
            ('extensao', models.ForeignKey(orm['cadastro.extensao'], null=False))
        ))
        db.create_unique(m2m_table_name, ['atividade_id', 'extensao_id'])


    def backwards(self, orm):
        # Deleting model 'Docente'
        db.delete_table('cadastro_docente')

        # Deleting model 'Disciplina'
        db.delete_table('cadastro_disciplina')

        # Deleting model 'Pesquisa'
        db.delete_table('cadastro_pesquisa')

        # Deleting model 'Extensao'
        db.delete_table('cadastro_extensao')

        # Deleting model 'Atividade'
        db.delete_table('cadastro_atividade')

        # Removing M2M table for field disciplinas on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_disciplinas'))

        # Removing M2M table for field pesquisa on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_pesquisa'))

        # Removing M2M table for field extensao on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_extensao'))


    models = {
        'cadastro.atividade': {
            'Meta': {'object_name': 'Atividade'},
            'afastamento': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comissoes': ('django.db.models.fields.IntegerField', [], {}),
            'disciplinas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cadastro.Disciplina']", 'symmetrical': 'False'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'extensao': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cadastro.Extensao']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pesquisa': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cadastro.Pesquisa']", 'symmetrical': 'False'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'cadastro.disciplina': {
            'Meta': {'object_name': 'Disciplina'},
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'estudantes': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multicampia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        'cadastro.docente': {
            'Meta': {'object_name': 'Docente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '7', 'unique': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'cadastro.extensao': {
            'Meta': {'object_name': 'Extensao'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'})
        },
        'cadastro.pesquisa': {
            'Meta': {'object_name': 'Pesquisa'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibic': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['cadastro']