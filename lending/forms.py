# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput, ModelChoiceField, CharField, \
    HiddenInput, DateField
from django.forms.extras.widgets import SelectDateWidget, Select
from django.forms.widgets import PasswordInput, TextInput
from django.utils import timezone
from django.utils.translation import ugettext as _
from lending.models import Lending, BookItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class LexiAuthenticationForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(widget=PasswordInput(attrs={'class':'form-control'})) 


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

    def __init__(self, book, user, *args, **kwargs):
        super(AddLendingForm, self).__init__(*args, **kwargs)
        self.fields['book_item'].queryset = BookItem.objects.filter(
            book=book, borrowed=False)
        self.fields['book_item'].initial = BookItem.objects.filter(
            book=book, borrowed=False).first()
        self.fields['book_item'].empty_label = None
        self.fields['start_date'].initial = timezone.now()


class AddLendingToSelfForm(ModelForm):
    user = UserFullNameChoiceField(label='', queryset=User.objects.order_by('last_name'),
        widget=HiddenInput)

    class Meta:
        model = Lending
        fields = ['user', 'book_item', 'start_date']
        widgets = {
            'book_item' : Select(attrs={'class':'form-control'}),
            'start_date': SelectDateWidget(attrs={'class':'form-control'})
        }

    def __init__(self, book, user, *args, **kwargs):
        super(AddLendingToSelfForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['start_date'].initial = timezone.now()
        self.fields['book_item'].queryset = BookItem.objects.filter(
            book=book, borrowed=False)
        self.fields['book_item'].initial = BookItem.objects.filter(
            book=book, borrowed=False).first()
        self.fields['book_item'].empty_label = None



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
        fields = ['user', 'book_item', 'start_date', 'end_date']
        widgets = {
            'book_item' : Select(attrs={'class':'form-control'}),
            'start_date': SelectDateWidget(attrs={'class':'form-control'}),
            'end_date': SelectDateWidget(attrs={'class':'form-control'})
        }