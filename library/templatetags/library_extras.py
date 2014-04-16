# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from library.forms import BookSearchForm




register = template.Library()


@register.filter
@stringfilter
def heart(value):
    return value + "<3"


@register.simple_tag()
def percentage(available, total):
    return int(float(available*100)/total)


@register.inclusion_tag('search.html')
def search(form_data=None):
    if form_data:
        form = BookSearchForm(form_data)
    else:
        form = BookSearchForm() 
    return { 'form': form }


@register.inclusion_tag('pagination.html')
def pagination(page_obj, queries={}):
    return { 'page_obj': page_obj,'queries': queries }


@register.inclusion_tag('book_list.html')
def book_list(object_list, search_performed=False):
    return { 'object_list': object_list, 'search_performed': search_performed }


@register.assignment_tag()
def century(year):
    if 1800 <= year < 1900:
        return 19
    elif 1900 <= year < 2000:
        return 20
    else:
        return 21


@register.inclusion_tag('users_lending_list.html')
def users_lending_list(object_list):
    return { 'object_list': object_list }


@register.inclusion_tag('lending_form.html')
def lending_form(form, button_text):
    return { 'form': form, 'button_text': button_text }


@register.inclusion_tag('navbar.html')
def navbar():
    return {}