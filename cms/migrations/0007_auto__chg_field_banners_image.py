# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Banners.image'
        db.alter_column('cms_banners', 'image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Banners.image'
        db.alter_column('cms_banners', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    models = {
        'cms.banners': {
            'Meta': {'object_name': 'Banners'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'cms.faq': {
            'Meta': {'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cms.homepageinfo': {
            'Meta': {'object_name': 'HomepageInfo'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_flyout': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'motto': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['cms']