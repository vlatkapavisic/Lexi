from django.contrib import admin
from library.models import *


class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publication_year',
		'get_authors','get_tags','category','language','get_number_of_book_items',
		'get_number_of_borrowed_book_items')
	search_fields = ['title','publication_year','authors__first_name', 
	'authors__last_name', 'tags__name', 'category__name','language']

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Book, BookAdmin)
