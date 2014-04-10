# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import ListView, View, TemplateView, CreateView
from django.views.generic.detail import DetailView
from lending.models import *
from library.models import *
from lending.forms import AddLendingForm



class LendingList(ListView):
    model = Lending
    template_name = 'lending/lendings.html'
    paginate_by = 10
    queryset = Lending.objects.order_by('-id')


class NewLending(CreateView):
    model = Lending
    template_name = 'lending/new_lending.html'
    form_class = AddLendingForm

    def get_success_url(self):
        return reverse('lending-added', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(NewLending, self).get_form_kwargs()
        self.book = Book.objects.get(pk=self.kwargs['book_pk'])
        kwargs['book'] = self.book
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(NewLending, self).get_context_data(**kwargs)
        context['book'] = self.book
        return context


class LendingAdded(TemplateView):
    template_name = "lending/lending_added.html"

    def get_context_data(self, **kwargs):
        context = super(LendingAdded, self).get_context_data(**kwargs)
        self.lending = Lending.objects.get(pk=self.kwargs['lending_pk']) 
        context['book_title'] = self.lending.book_item.book.title
        context['username'] = self.lending.user.username
        return context


class UsersCurrentLendings(ListView):
    model = Lending
    template_name = "lending/users_current_lendings.html"
    paginate_by = 3

    def get_queryset(self):
        self.user = User.objects.get(username=self.kwargs['username'])
        return Lending.objects.filter(user=self.user, end_date=None).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersCurrentLendings, self).get_context_data(**kwargs)
        context['username'] = self.user.username
        return context


class UsersLendings(ListView):
    model = Lending
    template_name = "lending/users_lendings.html"
    paginate_by = 10

    def get_queryset(self):
        self.user = User.objects.get(username=self.kwargs['username']) 
        return Lending.objects.filter(user=self.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersLendings, self).get_context_data(**kwargs)
        context['username'] = self.user.username
        return context


class UsersList(ListView):
    model = User
    template_name = "lending/users.html"
    paginate_by = 10
    queryset = User.objects.order_by('username')


