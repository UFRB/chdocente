# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Docente.centro'
        db.add_column('cadastro_docente', 'centro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=11),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Docente.centro'
        db.delete_column('cadastro_docente', 'centro')


    models = {
        'cadastro.atividade': {
            'Meta': {'object_name': 'Atividade'},
            'afastamento': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'comissoes': ('django.db.models.fields.IntegerField', [], {}),
            'disciplinas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cadastro.Disciplina']"}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'extensao': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cadastro.Extensao']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pesquisa': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cadastro.Pesquisa']"}),
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
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'})
        },
        'cadastro.pesquisa': {
            'Meta': {'object_name': 'Pesquisa'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2'})
        }
    }

    complete_apps = ['cadastro']