# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from library.models import *


class BookForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Book


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title','publication_year',
    	'get_authors','get_tags','category','language','total',
    	'available')
    filter_horizontal = ('authors', 'tags')
    search_fields = ['title','publication_year','authors__name',
     'tags__name', 'category__name']
 

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Book, BookAdmin)
