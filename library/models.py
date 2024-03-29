# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


__all__ = ('Author', 'Publisher', 'Category', 'Tag', 'Book')


class Author(models.Model):
    first_name = models.CharField(verbose_name=_(u"first name"), max_length=50)
    last_name = models.CharField(verbose_name=_(u"last name"), max_length=50)
    name = models.CharField(verbose_name=_(u"name"), blank=True, max_length=100)

    class Meta:
        verbose_name = _(u"author")
        verbose_name_plural = _(u"authors")
        ordering = ['last_name']

    def __unicode__(self):
        return self.name 

    def save(self, *args, **kwargs):
        self.name = self.first_name + " " + self.last_name
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author', args=[self.id])

    
class Publisher(models.Model):
    name = models.CharField(verbose_name=_(u"name"), max_length=200)

    class Meta:
        verbose_name = _(u"publisher")
        verbose_name_plural = _(u"publishers")
        ordering = ['name']
            
    def __unicode__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('publisher', args=[self.id])


class Category(models.Model): 
    name = models.CharField(verbose_name=_(u"name"), max_length=50)

    class Meta:
        verbose_name = _(u"category")
    	verbose_name_plural = _(u"categories")
        ordering = ['name']

    def __unicode__(self):
    	return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name=_(u"name"), max_length=50)

    class Meta:
        verbose_name = _(u"tag")
        verbose_name_plural = _(u"tags")
        ordering = ['name']

    def __unicode__(self):
    	return self.name


class Book(models.Model):
    LANGUAGE_CHOICES = (
        ('hr-HR',_(u'Croatian')),
        ('en-US',_(u'English')),
        ('de-DE',_(u'German')),
    )
    title = models.CharField(verbose_name=_(u"title"), max_length=200)
    description = models.CharField(verbose_name=_(u"description"),
        max_length=1000, blank=True)
    isbn = models.CharField(verbose_name="isbn", max_length=24)
    authors = models.ManyToManyField(Author, verbose_name=_(u"authors"), 
        related_name="books")
    publisher = models.ForeignKey(Publisher, verbose_name=_(u"publisher"), 
        related_name="books")
    publication_year = models.IntegerField(verbose_name=_(u"publication year"))
    cover_image = models.ImageField(upload_to='cover_images', blank=True, 
        verbose_name=_(u"cover image"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_(u"tags"), 
        related_name="books")
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, 
        verbose_name=_(u"language"))
    category = models.ForeignKey(Category, verbose_name=_(u"category"), 
        related_name="books")

    class Meta:
        verbose_name = _(u"book")
        verbose_name_plural = _(u"books")
        ordering = ['title']

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('book', args=[self.pk])

    def get_authors(self):
        return ", ".join([author.name for author in self.authors.all()]) 

    get_authors.short_description = _(u"authors")

    def get_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])

    get_tags.short_description = _(u"tags")

    def total(self):
        from lending.models import BookItem
    	return BookItem.objects.all().filter(book=self).count()

    def borrowed(self):
        from lending.models import BookItem
    	return BookItem.objects.all().filter(book=self, borrowed=True).count()

    def available(self):
        from lending.models import BookItem
        return BookItem.objects.all().filter(book=self, borrowed=False).count()


# class Wish(models.Model):
#     title = models.CharField(verbose_name=_(u"title"), max_length=200)
#     authors = models.CharField(verbose_name=_(u"authors"), max_length=200)
#     posted_by = models.ForeignKey(User)
#     date_added = models.DateField(verbose_name=_(u"date_added")) 
#     fullfilled = models.BooleanField(default=False, verbose_name=_(u"fullfilled"))

#     class Meta:
#         verbose_name = _(u"wish")
#         verbose_name_plural = _(u"wishes")
#         ordering = ['date_added']

#     def __unicode__(self):
#         return self.title

