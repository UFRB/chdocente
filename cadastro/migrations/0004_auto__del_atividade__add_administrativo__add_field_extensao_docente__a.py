# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Atividade'
        db.delete_table('cadastro_atividade')

        # Removing M2M table for field pesquisa on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_pesquisa'))

        # Removing M2M table for field extensao on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_extensao'))

        # Removing M2M table for field disciplinas on 'Atividade'
        db.delete_table(db.shorten_name('cadastro_atividade_disciplinas'))

        # Adding model 'Administrativo'
        db.create_table('cadastro_administrativo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'])),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('afastamento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cargo', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('comissoes', self.gf('django.db.models.fields.IntegerField')(blank=True, max_length=2, null=True)),
        ))
        db.send_create_signal('cadastro', ['Administrativo'])

        # Adding field 'Extensao.docente'
        db.add_column('cadastro_extensao', 'docente',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'], default=0),
                      keep_default=False)

        # Adding field 'Extensao.semestre'
        db.add_column('cadastro_extensao', 'semestre',
                      self.gf('django.db.models.fields.CharField')(max_length=6, default=0),
                      keep_default=False)

        # Adding field 'Pesquisa.docente'
        db.add_column('cadastro_pesquisa', 'docente',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'], default=0),
                      keep_default=False)

        # Adding field 'Pesquisa.semestre'
        db.add_column('cadastro_pesquisa', 'semestre',
                      self.gf('django.db.models.fields.CharField')(max_length=6, default=0),
                      keep_default=False)

        # Adding field 'Disciplina.docente'
        db.add_column('cadastro_disciplina', 'docente',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'], default=0),
                      keep_default=False)

        # Adding field 'Disciplina.semestre'
        db.add_column('cadastro_disciplina', 'semestre',
                      self.gf('django.db.models.fields.CharField')(max_length=6, default=0),
                      keep_default=False)

        # Adding field 'Disciplina.nome'
        db.add_column('cadastro_disciplina', 'nome',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Atividade'
        db.create_table('cadastro_atividade', (
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastro.Docente'])),
            ('cargo', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('comissoes', self.gf('django.db.models.fields.IntegerField')(blank=True, max_length=2, null=True)),
            ('afastamento', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cadastro', ['Atividade'])

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

        # Adding M2M table for field disciplinas on 'Atividade'
        m2m_table_name = db.shorten_name('cadastro_atividade_disciplinas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('atividade', models.ForeignKey(orm['cadastro.atividade'], null=False)),
            ('disciplina', models.ForeignKey(orm['cadastro.disciplina'], null=False))
        ))
        db.create_unique(m2m_table_name, ['atividade_id', 'disciplina_id'])

        # Deleting model 'Administrativo'
        db.delete_table('cadastro_administrativo')

        # Deleting field 'Extensao.docente'
        db.delete_column('cadastro_extensao', 'docente_id')

        # Deleting field 'Extensao.semestre'
        db.delete_column('cadastro_extensao', 'semestre')

        # Deleting field 'Pesquisa.docente'
        db.delete_column('cadastro_pesquisa', 'docente_id')

        # Deleting field 'Pesquisa.semestre'
        db.delete_column('cadastro_pesquisa', 'semestre')

        # Deleting field 'Disciplina.docente'
        db.delete_column('cadastro_disciplina', 'docente_id')

        # Deleting field 'Disciplina.semestre'
        db.delete_column('cadastro_disciplina', 'semestre')

        # Deleting field 'Disciplina.nome'
        db.delete_column('cadastro_disciplina', 'nome')


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
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
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
            'bolsistas_pibex': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'bolsistas_ppq': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
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