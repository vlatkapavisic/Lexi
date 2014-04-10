# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateInput
from django.forms.extras.widgets import SelectDateWidget, Select
from lending.models import Lending, BookItem
from datetime import date
from django.utils import timezone
from django.utils.translation import ugettext as _

class AddLendingForm(ModelForm):
    class Meta:
        model = Lending
        fields = ['user', 'book_item', 'start_date']
        widgets = {
            'user' : Select(attrs={'class':'form-control',}),
            'book_item' : Select(attrs={'class':'form-control',}),
            'start_date': SelectDateWidget(attrs={'class':'form-control','style':'display:inline'})
        }

    def __init__(self, book, *args, **kwargs):
        super(AddLendingForm, self).__init__(*args, **kwargs)
        self.fields['book_item'].queryset = BookItem.objects.filter(
            book=book, borrowed=False)
        self.fields['book_item'].initial = BookItem.objects.filter(
            book=book, borrowed=False).first()
        self.fields['start_date'].initial = timezone.now()


