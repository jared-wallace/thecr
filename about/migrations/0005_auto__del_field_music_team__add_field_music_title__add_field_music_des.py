# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Music.team'
        db.delete_column('about_music', 'team_id')

        # Adding field 'Music.title'
        db.add_column('about_music', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Music.description'
        db.add_column('about_music', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Music.date_recorded'
        db.add_column('about_music', 'date_recorded',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 8, 0, 0)),
                      keep_default=False)

        # Deleting field 'Video.team'
        db.delete_column('about_video', 'team_id')

        # Adding field 'Video.title'
        db.add_column('about_video', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Video.description'
        db.add_column('about_video', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Music.team'
        db.add_column('about_music', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='mp3s', to=orm['about.WorshipTeam']),
                      keep_default=False)

        # Deleting field 'Music.title'
        db.delete_column('about_music', 'title')

        # Deleting field 'Music.description'
        db.delete_column('about_music', 'description')

        # Deleting field 'Music.date_recorded'
        db.delete_column('about_music', 'date_recorded')

        # Adding field 'Video.team'
        db.add_column('about_video', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='videos', to=orm['about.WorshipTeam']),
                      keep_default=False)

        # Deleting field 'Video.title'
        db.delete_column('about_video', 'title')

        # Deleting field 'Video.description'
        db.delete_column('about_video', 'description')


    models = {
        'about.beliefs': {
            'Meta': {'object_name': 'Beliefs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'about.music': {
            'Meta': {'object_name': 'Music'},
            'date_recorded': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'about.pastor': {
            'Meta': {'object_name': 'Pastor'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'about.sermonseries': {
            'Meta': {'object_name': 'SermonSeries'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'about.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'about.worshipteam': {
            'Meta': {'object_name': 'WorshipTeam'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['about']