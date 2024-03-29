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
    if total == 0:
        return 0
    else:
        return int(float(available*100)/total)


@register.inclusion_tag('template_tags/advanced_search.html')
def advanced_search(form_data=None):
    if form_data:
        form = BookSearchForm(form_data)
    else:
        form = BookSearchForm() 
    return { 'form': form }


@register.inclusion_tag('template_tags/pagination.html')
def pagination(page_obj, queries={}):
    last = page_obj.paginator.page_range[-1]
    start = page_obj.number
    if start == last - 1:
        start -= 1
    elif start == last:
        start -= 2
    pagination_range = range(start, start + 3)
    return { 'page_obj': page_obj,'queries': queries, 'pagination_range': 
        pagination_range, 'last': last }


@register.inclusion_tag('template_tags/book_list.html')
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


@register.inclusion_tag('template_tags/users_lending_list.html')
def users_lending_list(object_list, perms):
    return { 'object_list': object_list, 'perms':perms }


@register.inclusion_tag('template_tags/lending_form.html')
def lending_form(form, button_text):
    return { 'form': form, 'button_text': button_text }


@register.inclusion_tag('template_tags/navbar.html')
def navbar(user, perms):
    return {'user':user, 'perms':perms}


@register.inclusion_tag('template_tags/simple_search.html', takes_context=True)
def simple_search(context):
    data = {
        'search_performed': context.get('search_performed'),
        'search_term': context.get('search_term')
    }
    return data


