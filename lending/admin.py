from django.contrib import admin
from lending.models import *


class BookItemAdmin(admin.ModelAdmin):
   list_display = ('item_id','book_title','borrowed','get_borrower',)
   exclude = ('borrowed','item_id')

   def save_model(self, request, obj, form, change):
      try:
         latest_item = BookItem.objects.filter(book=obj.book).latest('item_id')
         obj.item_id = latest_item.item_id + 1
      except:
         obj.item_id = 1
      obj.save()

class LendingAdmin(admin.ModelAdmin):
	list_display = ('book_title','user_name','start_date','end_date',)

	def save_model(self, request, obj, form, change):
   		if obj.end_date is not None:
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