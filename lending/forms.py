# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput, ModelChoiceField
from django.forms.extras.widgets import SelectDateWidget, Select
from django.utils import timezone
from django.utils.translation import ugettext as _
from datetime import date
from lending.models import Lending, BookItem


class UserFullNameChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + " " + obj.last_name


class AddLendingForm(ModelForm):
    user = UserFullNameChoiceField(User.objects.order_by('last_name'), 
        widget=Select(attrs={'class':'form-control'}))

    class Meta:
        model = Lending
        fields = ['user', 'book_item', 'start_date']
        widgets = {
            'user' : Select(attrs={'class':'form-control'}),
            'book_item' : Select(attrs={'class':'form-control'}),
            'start_date': SelectDateWidget(attrs={'class':'form-control'})
        }

    def __init__(self, book, *args, **kwargs):
        super(AddLendingForm, self).__init__(*args, **kwargs)
        self.fields['book_item'].queryset = BookItem.objects.filter(
            book=book, borrowed=False)
        self.fields['book_item'].initial = BookItem.objects.filter(
            book=book, borrowed=False).first()
        self.fields['start_date'].initial = timezone.now()


class FinishLendingForm(ModelForm):
    class Meta:
        model = Lending
        fields = ['end_date']
        widgets = {
            'end_date': SelectDateWidget(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(FinishLendingForm, self).__init__(*args, **kwargs)
        self.initial['end_date'] = timezone.now()


class EditLendingForm(ModelForm):
    user = UserFullNameChoiceField(User.objects.order_by('last_name'), 
        widget=Select(attrs={'class':'form-control'}))

    class Meta:
        model = Lending
        fields = ['user', 'book_item', 'start_date']
        widgets = {
            'book_item' : Select(attrs={'class':'form-control'}),
            'start_date': SelectDateWidget(attrs={'class':'form-control'})
        }
        

