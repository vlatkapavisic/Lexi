# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BookItem.borrowed'
        db.add_column(u'lending_bookitem', 'borrowed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BookItem.borrowed'
        db.delete_column(u'lending_bookitem', 'borrowed')


    models = {
        u'lending.bookitem': {
            'Meta': {'object_name': 'BookItem'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            'borrowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lending.lending': {
            'Meta': {'object_name': 'Lending'},
            'book_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lending.BookItem']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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