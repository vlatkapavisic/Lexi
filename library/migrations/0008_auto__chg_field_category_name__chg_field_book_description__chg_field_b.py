# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column(u'library_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Book.description'
        db.alter_column(u'library_book', 'description', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Book.title'
        db.alter_column(u'library_book', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Publisher.name'
        db.alter_column(u'library_publisher', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Adding field 'Author.name'
        db.add_column(u'library_author', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


        # Changing field 'Author.first_name'
        db.alter_column(u'library_author', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Author.last_name'
        db.alter_column(u'library_author', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column(u'library_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Book.description'
        db.alter_column(u'library_book', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Book.title'
        db.alter_column(u'library_book', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Publisher.name'
        db.alter_column(u'library_publisher', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'Author.name'
        db.delete_column(u'library_author', 'name')


        # Changing field 'Author.first_name'
        db.alter_column(u'library_author', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Author.last_name'
        db.alter_column(u'library_author', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'library.author': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'library.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'books'", 'symmetrical': 'False', 'to': u"orm['library.Author']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': u"orm['library.Category']"}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'publication_year': ('django.db.models.fields.IntegerField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': u"orm['library.Publisher']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'books'", 'blank': 'True', 'to': u"orm['library.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'library.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'library.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['library']