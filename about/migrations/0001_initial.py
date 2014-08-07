# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pastor'
        db.create_table('about_pastor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('about', ['Pastor'])

        # Adding model 'Beliefs'
        db.create_table('about_beliefs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('about', ['Beliefs'])

        # Adding model 'WorshipTeam'
        db.create_table('about_worshipteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('leader', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='leads', null=True, to=orm['auth.User'])),
            ('drummer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='plays_drums', null=True, to=orm['auth.User'])),
            ('bassist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='plays_bass', null=True, to=orm['auth.User'])),
            ('guitarist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='plays_guitar', null=True, to=orm['auth.User'])),
            ('saxophonist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='plays_sax', null=True, to=orm['auth.User'])),
            ('pianist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='plays_piano', null=True, to=orm['auth.User'])),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('about', ['WorshipTeam'])

        # Adding model 'Video'
        db.create_table('about_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['about.WorshipTeam'])),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('about', ['Video'])

        # Adding model 'Music'
        db.create_table('about_music', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mp3s', to=orm['about.WorshipTeam'])),
            ('music', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('about', ['Music'])

        # Adding model 'SermonSeries'
        db.create_table('about_sermonseries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('about', ['SermonSeries'])


    def backwards(self, orm):
        # Deleting model 'Pastor'
        db.delete_table('about_pastor')

        # Deleting model 'Beliefs'
        db.delete_table('about_beliefs')

        # Deleting model 'WorshipTeam'
        db.delete_table('about_worshipteam')

        # Deleting model 'Video'
        db.delete_table('about_video')

        # Deleting model 'Music'
        db.delete_table('about_music')

        # Deleting model 'SermonSeries'
        db.delete_table('about_sermonseries')


    models = {
        'about.beliefs': {
            'Meta': {'object_name': 'Beliefs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'about.music': {
            'Meta': {'object_name': 'Music'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mp3s'", 'to': "orm['about.WorshipTeam']"})
        },
        'about.pastor': {
            'Meta': {'object_name': 'Pastor'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'about.sermonseries': {
            'Meta': {'object_name': 'SermonSeries'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'about.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['about.WorshipTeam']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'about.worshipteam': {
            'Meta': {'object_name': 'WorshipTeam'},
            'bassist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plays_bass'", 'null': 'True', 'to': "orm['auth.User']"}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'drummer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plays_drums'", 'null': 'True', 'to': "orm['auth.User']"}),
            'guitarist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plays_guitar'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'leads'", 'null': 'True', 'to': "orm['auth.User']"}),
            'pianist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plays_piano'", 'null': 'True', 'to': "orm['auth.User']"}),
            'saxophonist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plays_sax'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']