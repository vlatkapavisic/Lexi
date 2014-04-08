# -*- coding: utf-8 -*-

from django.contrib import admin
from library.models import *


class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publication_year',
		'get_authors','get_tags','category','language','get_number_of_book_items',
		'get_number_of_available_book_items')
	filter_horizontal = ('authors', 'tags')
	search_fields = ['title','publication_year','authors__first_name', 
	'authors__last_name', 'tags__name', 'category__name']
 

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Book, BookAdmin)
