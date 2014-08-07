# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomepageInfo'
        db.create_table('cms_homepageinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.TextField')(max_length=13)),
            ('email', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('facebook', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('twitter', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('address1', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('address2', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('address3', self.gf('django.db.models.fields.TextField')(max_length=100)),
        ))
        db.send_create_signal('cms', ['HomepageInfo'])


    def backwards(self, orm):
        # Deleting model 'HomepageInfo'
        db.delete_table('cms_homepageinfo')


    models = {
        'cms.banners': {
            'Meta': {'object_name': 'Banners'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'address1': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'address3': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.TextField', [], {'max_length': '13'}),
            'twitter': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['cms']