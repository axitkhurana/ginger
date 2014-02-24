# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.fb_id'
        db.add_column(u'foodie_event', 'fb_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.fb_id'
        db.delete_column(u'foodie_event', 'fb_id')


    models = {
        u'foodie.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'vendors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['foodie.Vendor']", 'null': 'True', 'blank': 'True'})
        },
        u'foodie.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['foodie']