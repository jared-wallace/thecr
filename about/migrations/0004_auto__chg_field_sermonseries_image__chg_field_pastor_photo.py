# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SermonSeries.image'
        db.alter_column('about_sermonseries', 'image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True))

        # Changing field 'Pastor.photo'
        db.alter_column('about_pastor', 'photo', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'SermonSeries.image'
        db.alter_column('about_sermonseries', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Pastor.photo'
        db.alter_column('about_pastor', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

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