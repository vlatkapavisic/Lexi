from django.contrib import admin
from lending.models import *


class BookItemAdmin(admin.ModelAdmin):
   list_display = ('id','book_title','borrowed','get_borrower',)
   exclude = ('borrowed',)

class LendingAdmin(admin.ModelAdmin):
	list_display = ('book_title','user_name','start_date','end_date',)
	#fields =  ('available_books','user_name','start_date','end_date')

	def save_model(self, request, obj, form, change):
   		if change:
   			obj.book_item.borrowed = False
   		else:
   			obj.book_item.borrowed = True
   		obj.book_item.save()
   		obj.save()

class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name')

admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Lending, LendingAdmin)
admin.site.register(User, UserAdmin)