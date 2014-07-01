# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Extensao.cargahoraria'
        db.add_column('cadastro_extensao', 'cargahoraria',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, max_length=3, default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Extensao.cargahoraria'
        db.delete_column('cadastro_extensao', 'cargahoraria')


    models = {
        'cadastro.administrativo': {
            'Meta': {'object_name': 'Administrativo'},
            'afastamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'comissoes': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'cadastro.disciplina': {
            'Meta': {'object_name': 'Disciplina'},
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'estudantes': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multicampia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
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
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'})
        },
        'cadastro.pesquisa': {
            'Meta': {'object_name': 'Pesquisa'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parceria': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'})
        }
    }

    complete_apps = ['cadastro']