# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pesquisa.nome'
        db.add_column('cadastro_pesquisa', 'nome',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default='semnome'),
                      keep_default=False)

        # Adding field 'Extensao.nome'
        db.add_column('cadastro_extensao', 'nome',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default='semnome'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pesquisa.nome'
        db.delete_column('cadastro_pesquisa', 'nome')

        # Deleting field 'Extensao.nome'
        db.delete_column('cadastro_extensao', 'nome')


    models = {
        'cadastro.administrativo': {
            'Meta': {'object_name': 'Administrativo'},
            'afastamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comissoes': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
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
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '7', 'unique': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'cadastro.extensao': {
            'Meta': {'object_name': 'Extensao'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parceria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'cadastro.pesquisa': {
            'Meta': {'object_name': 'Pesquisa'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bolsistas_pibic': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cargahoraria': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cadastro.Docente']"}),
            'estudantes_graduacao': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'estudantes_pos': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parceria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parceria_inter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'voluntarios': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cadastro']