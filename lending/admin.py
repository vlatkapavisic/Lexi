# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms.extras.widgets import Select
from django.utils import timezone
from lending.models import *
from library.models import *


class BookItemAdmin(admin.ModelAdmin):
	list_display = ('item_id','book','borrowed','borrowed_by')
	list_filter = ('borrowed','book')
	exclude = ('item_id','borrowed')


class UserFullNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + " " + obj.last_name
    

class LendingAdminForm(forms.ModelForm):
	user = UserFullNameChoiceField(User.objects.order_by('last_name'), 
        widget=Select(attrs={'class':'form-control'}))

	class Meta:
		model = Lending

	def __init__(self, *args, **kwargs):
		super(LendingAdminForm, self).__init__(*args, **kwargs)
		if not self.instance.pk: 
			self.fields['book_item'].queryset = BookItem.objects. \
			filter(borrowed=False)


class LendingAdmin(admin.ModelAdmin):
	form = LendingAdminForm
	list_display = ('book_item','borrowed_by','start_date','end_date')
	list_filter = ('user','book_item__book')


admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Lending, LendingAdmin)