# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table(u'foodie_vendor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'foodie', ['Vendor'])

        # Adding model 'Event'
        db.create_table(u'foodie_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'foodie', ['Event'])

        # Adding M2M table for field vendors on 'Event'
        m2m_table_name = db.shorten_name(u'foodie_event_vendors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'foodie.event'], null=False)),
            ('vendor', models.ForeignKey(orm[u'foodie.vendor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'vendor_id'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table(u'foodie_vendor')

        # Deleting model 'Event'
        db.delete_table(u'foodie_event')

        # Removing M2M table for field vendors on 'Event'
        db.delete_table(db.shorten_name(u'foodie_event_vendors'))


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['foodie']