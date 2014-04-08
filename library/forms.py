from django import forms
from library.models import Book
from datetime import date
from django.utils.translation import ugettext as _


class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, label=_("Title"), max_length=100)
    authors = forms.CharField(required=False, label=_("Author(s)"), 
        help_text=_("Separate multiple authors with commas."), max_length=100)
    publisher = forms.CharField(required=False, label=_("Publisher"), max_length=100)
    tags = forms.CharField(required=False, label=_("Tag(s)"),
        help_text=_("Separate multiple tags with commas."), max_length=100)
    category = forms.CharField(required=False, label=_("Category"), max_length=100)
    