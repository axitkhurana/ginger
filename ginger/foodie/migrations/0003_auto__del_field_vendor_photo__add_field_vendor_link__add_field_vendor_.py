# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Vendor.photo'
        db.delete_column(u'foodie_vendor', 'photo')

        # Adding field 'Vendor.link'
        db.add_column(u'foodie_vendor', 'link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Vendor.photo_url'
        db.add_column(u'foodie_vendor', 'photo_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Vendor.type'
        db.alter_column(u'foodie_vendor', 'type', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Adding field 'Vendor.photo'
        db.add_column(u'foodie_vendor', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Vendor.link'
        db.delete_column(u'foodie_vendor', 'link')

        # Deleting field 'Vendor.photo_url'
        db.delete_column(u'foodie_vendor', 'photo_url')


        # Changing field 'Vendor.type'
        db.alter_column(u'foodie_vendor', 'type', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'foodie.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'vendors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['foodie.Vendor']", 'symmetrical': 'False'})
        },
        u'foodie.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['foodie']