# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'library_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'library', ['Category'])

        # Adding model 'Publisher'
        db.create_table(u'library_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'library', ['Publisher'])

        # Adding model 'Tag'
        db.create_table(u'library_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'library', ['Tag'])

        # Adding model 'Book'
        db.create_table(u'library_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Publisher'])),
            ('publication_year', self.gf('django.db.models.fields.IntegerField')()),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Category'])),
        ))
        db.send_create_signal(u'library', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'library_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'library.book'], null=False)),
            ('author', models.ForeignKey(orm[u'library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding M2M table for field tags on 'Book'
        m2m_table_name = db.shorten_name(u'library_book_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'library.book'], null=False)),
            ('tag', models.ForeignKey(orm[u'library.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'tag_id'])

        # Adding model 'Author'
        db.create_table(u'library_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'library', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'library_category')

        # Deleting model 'Publisher'
        db.delete_table(u'library_publisher')

        # Deleting model 'Tag'
        db.delete_table(u'library_tag')

        # Deleting model 'Book'
        db.delete_table(u'library_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'library_book_authors'))

        # Removing M2M table for field tags on 'Book'
        db.delete_table(db.shorten_name(u'library_book_tags'))

        # Deleting model 'Author'
        db.delete_table(u'library_author')


    models = {
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
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
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

    complete_apps = ['library']