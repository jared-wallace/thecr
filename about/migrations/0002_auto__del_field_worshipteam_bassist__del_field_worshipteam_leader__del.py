# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'WorshipTeam.bassist'
        db.delete_column('about_worshipteam', 'bassist_id')

        # Deleting field 'WorshipTeam.leader'
        db.delete_column('about_worshipteam', 'leader_id')

        # Deleting field 'WorshipTeam.saxophonist'
        db.delete_column('about_worshipteam', 'saxophonist_id')

        # Deleting field 'WorshipTeam.guitarist'
        db.delete_column('about_worshipteam', 'guitarist_id')

        # Deleting field 'WorshipTeam.drummer'
        db.delete_column('about_worshipteam', 'drummer_id')

        # Deleting field 'WorshipTeam.pianist'
        db.delete_column('about_worshipteam', 'pianist_id')


    def backwards(self, orm):
        # Adding field 'WorshipTeam.bassist'
        db.add_column('about_worshipteam', 'bassist',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='plays_bass', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'WorshipTeam.leader'
        db.add_column('about_worshipteam', 'leader',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='leads', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'WorshipTeam.saxophonist'
        db.add_column('about_worshipteam', 'saxophonist',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='plays_sax', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'WorshipTeam.guitarist'
        db.add_column('about_worshipteam', 'guitarist',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='plays_guitar', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'WorshipTeam.drummer'
        db.add_column('about_worshipteam', 'drummer',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='plays_drums', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'WorshipTeam.pianist'
        db.add_column('about_worshipteam', 'pianist',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='plays_piano', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['about']