# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from library.models import Book
from django.utils import timezone


__all__ = ('BookItem', 'Lending')
    

class BookItem(models.Model):
    book = models.ForeignKey(Book, verbose_name=_(u"book"), related_name="book_items")
    borrowed = models.BooleanField(default=False, verbose_name=_(u"borrowed"))
    item_id = models.IntegerField(verbose_name=_(u"item ID"))

    class Meta:
        verbose_name = _(u"book item")
        verbose_name_plural = _(u"book items")
        unique_together = ('book','item_id')
        ordering = ['book','item_id']

    def __unicode__(self):
        return u"{0} ({1})".format(self.book.title, str(self.item_id))

    def save(self, *args, **kwargs):
        if self.pk is None:  #prvo spremanje, novi objekt
            try:
                latest_item = BookItem.objects.filter(book=self.book).order_by('-item_id')[0]
                self.item_id = latest_item.item_id + 1
            except IndexError:
                self.item_id = 1
        super(BookItem, self).save(*args, **kwargs)

    def book_title(self):
        return self.book.title

    def get_borrower(self):
        if self.borrowed:
            u = Lending.objects.filter(book_item=self).first().user
            return u.username
        else:
            return ""

    get_borrower.short_description = _(u'borrowed by')


class Lending(models.Model):
    book_item = models.ForeignKey(BookItem, verbose_name=_(u"book item"), related_name="book_item")
    user = models.ForeignKey(User)
    start_date = models.DateField(verbose_name=_(u"start date")) 
    end_date = models.DateField(blank=True, null=True, verbose_name=_(u"end date")) 

    class Meta:
        verbose_name = _(u"lending")
        verbose_name_plural = _(u"lendings")
        ordering = ['-start_date']

    def __unicode__(self):
        return self.book_title()

    def save(self, *args, **kwargs):
        if self.end_date:
            self.book_item.borrowed = False
        else:
            self.book_item.borrowed = True
        self.book_item.save()
        super(Lending, self).save(*args, **kwargs)
      
    def book_title(self):
        return self.book_item.book.title

    def user_name(self):
        return self.user.username
   

@receiver(pre_delete, sender=Lending)
def unborrow(sender, **kwargs):
    lending = kwargs['instance']
    lending.book_item.borrowed = False
    lending.book_item.save()