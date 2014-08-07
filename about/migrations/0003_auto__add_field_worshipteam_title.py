# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorshipTeam.title'
        db.add_column('about_worshipteam', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorshipTeam.title'
        db.delete_column('about_worshipteam', 'title')


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
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['about']