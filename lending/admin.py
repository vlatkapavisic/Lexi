# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from lending.models import *
from library.models import *
from django.utils import timezone


class BookItemAdmin(admin.ModelAdmin):
	list_display = ('item_id','book','borrowed','get_borrower')
	exclude = ('item_id','borrowed')
	list_filter = ('borrowed',)


class LendingAdminForm(forms.ModelForm):
	class Meta:
		model = Lending

	def __init__(self, *args, **kwargs):
		super(LendingAdminForm, self).__init__(*args, **kwargs)
		if not self.instance.pk: 
			self.fields['book_item'].queryset = BookItem.objects.filter(borrowed=False)


class LendingAdmin(admin.ModelAdmin):
	list_display = ('book_item','user_name','start_date','end_date')
	form = LendingAdminForm

	# def delete_model(self, request, obj):
	# 	book_item = obj.book_item
	# 	book_item.borrowed = False
	# 	book_item.save()
	# 	super(LendingAdmin, self).delete_model(request, obj)



admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Lending, LendingAdmin)