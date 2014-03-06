# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'lending_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'lending', ['User'])

        # Adding model 'BookItem'
        db.create_table(u'lending_bookitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
        ))
        db.send_create_signal(u'lending', ['BookItem'])

        # Adding model 'Lending'
        db.create_table(u'lending_lending', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lending.BookItem'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lending.User'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'lending', ['Lending'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'lending_user')

        # Deleting model 'BookItem'
        db.delete_table(u'lending_bookitem')

        # Deleting model 'Lending'
        db.delete_table(u'lending_lending')


    models = {
        u'lending.bookitem': {
            'Meta': {'object_name': 'BookItem'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lending.lending': {
            'Meta': {'object_name': 'Lending'},
            'book_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lending.BookItem']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lending.User']"})
        },
        u'lending.user': {
            'Meta': {'object_name': 'User'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Category']"}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'publication_year': ('django.db.models.fields.IntegerField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'library.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['lending']