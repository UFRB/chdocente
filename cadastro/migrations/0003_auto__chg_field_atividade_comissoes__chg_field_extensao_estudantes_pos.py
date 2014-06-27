# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Atividade.comissoes'
        db.alter_column('cadastro_atividade', 'comissoes', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.estudantes_pos'
        db.alter_column('cadastro_extensao', 'estudantes_pos', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.voluntarios'
        db.alter_column('cadastro_extensao', 'voluntarios', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.estudantes_graduacao'
        db.alter_column('cadastro_extensao', 'estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.bolsistas_ppq'
        db.alter_column('cadastro_extensao', 'bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.bolsistas_pibex'
        db.alter_column('cadastro_extensao', 'bolsistas_pibex', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Extensao.parceria_inter'
        db.alter_column('cadastro_extensao', 'parceria_inter', self.gf('django.db.models.fields.CharField')(null=True, max_length=255))

        # Changing field 'Pesquisa.estudantes_pos'
        db.alter_column('cadastro_pesquisa', 'estudantes_pos', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Pesquisa.voluntarios'
        db.alter_column('cadastro_pesquisa', 'voluntarios', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Pesquisa.estudantes_graduacao'
        db.alter_column('cadastro_pesquisa', 'estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Pesquisa.bolsistas_ppq'
        db.alter_column('cadastro_pesquisa', 'bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Pesquisa.bolsistas_pibic'
        db.alter_column('cadastro_pesquisa', 'bolsistas_pibic', self.gf('django.db.models.fields.IntegerField')(null=True, max_length=2))

        # Changing field 'Pesquisa.parceria_inter'
        db.alter_column('cadastro_pesquisa', 'parceria_inter', self.gf('django.db.models.fields.CharField')(null=True, max_length=255))

    def backwards(self, orm):

        # Changing field 'Atividade.comissoes'
        db.alter_column('cadastro_atividade', 'comissoes', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Extensao.estudantes_pos'
        db.alter_column('cadastro_extensao', 'estudantes_pos', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Extensao.voluntarios'
        db.alter_column('cadastro_extensao', 'voluntarios', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Extensao.estudantes_graduacao'
        db.alter_column('cadastro_extensao', 'estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Extensao.bolsistas_ppq'
        db.alter_column('cadastro_extensao', 'bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Extensao.bolsistas_pibex'
        db.alter_column('cadastro_extensao', 'bolsistas_pibex', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Extensao.parceria_inter'
        db.alter_column('cadastro_extensao', 'parceria_inter', self.gf('django.db.models.fields.CharField')(max_length=255, default=''))

        # Changing field 'Pesquisa.estudantes_pos'
        db.alter_column('cadastro_pesquisa', 'estudantes_pos', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Pesquisa.voluntarios'
        db.alter_column('cadastro_pesquisa', 'voluntarios', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Pesquisa.estudantes_graduacao'
        db.alter_column('cadastro_pesquisa', 'estudantes_graduacao', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Pesquisa.bolsistas_ppq'
        db.alter_column('cadastro_pesquisa', 'bolsistas_ppq', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Pesquisa.bolsistas_pibic'
        db.alter_column('cadastro_pesquisa', 'bolsistas_pibic', self.gf('django.db.models.fields.IntegerField')(max_length=2, default=0))

        # Changing field 'Pesquisa.parceria_inter'
        db.alter_column('cadastro_pesquisa', 'parceria_inter', self.gf('django.db.models.fields.CharField')(max_length=255, default=''))

    models = {
        'cadastro.atividade': {
            'Meta': {'object_name': 'Atividade'},
            'afastamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'comissoes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
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
            'centro': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '7'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'cadastro.extensao': {
            'Meta': {'object_name': 'Extensao'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'})
        },
        'cadastro.pesquisa': {
            'Meta': {'object_name': 'Pesquisa'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['cadastro']