# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HomepageInfo.motto'
        db.add_column('cms_homepageinfo', 'motto',
                      self.gf('django.db.models.fields.TextField')(default='Not your ordinary church', max_length=500),
                      keep_default=False)


        # Changing field 'HomepageInfo.address2'
        db.alter_column('cms_homepageinfo', 'address2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomepageInfo.address1'
        db.alter_column('cms_homepageinfo', 'address1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomepageInfo.twitter'
        db.alter_column('cms_homepageinfo', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HomepageInfo.address3'
        db.alter_column('cms_homepageinfo', 'address3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomepageInfo.phone'
        db.alter_column('cms_homepageinfo', 'phone', self.gf('django.db.models.fields.CharField')(max_length=14))

        # Changing field 'HomepageInfo.facebook'
        db.alter_column('cms_homepageinfo', 'facebook', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HomepageInfo.email'
        db.alter_column('cms_homepageinfo', 'email', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'HomepageInfo.motto'
        db.delete_column('cms_homepageinfo', 'motto')


        # Changing field 'HomepageInfo.address2'
        db.alter_column('cms_homepageinfo', 'address2', self.gf('django.db.models.fields.TextField')(max_length=100))

        # Changing field 'HomepageInfo.address1'
        db.alter_column('cms_homepageinfo', 'address1', self.gf('django.db.models.fields.TextField')(max_length=100))

        # Changing field 'HomepageInfo.twitter'
        db.alter_column('cms_homepageinfo', 'twitter', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Changing field 'HomepageInfo.address3'
        db.alter_column('cms_homepageinfo', 'address3', self.gf('django.db.models.fields.TextField')(max_length=100))

        # Changing field 'HomepageInfo.phone'
        db.alter_column('cms_homepageinfo', 'phone', self.gf('django.db.models.fields.TextField')(max_length=14))

        # Changing field 'HomepageInfo.facebook'
        db.alter_column('cms_homepageinfo', 'facebook', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Changing field 'HomepageInfo.email'
        db.alter_column('cms_homepageinfo', 'email', self.gf('django.db.models.fields.TextField')(max_length=100))

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
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motto': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['cms']