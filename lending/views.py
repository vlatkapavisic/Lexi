# -*- coding: utf-8 -*-

from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import ListView, View, TemplateView, CreateView, \
                                UpdateView
from django.views.generic.detail import DetailView
from lending.models import *
from library.models import *
from lending.forms import AddLendingForm, FinishLendingForm, EditLendingForm



class LendingList(ListView):
    model = Lending
    template_name = 'lending/lendings.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Lending.objects.all()
        self.search_performed = False
        self.search_term = self.request.GET.get('search')
        if self.search_term:
            self.search_performed = True
            return queryset.filter(Q(book_item__book__title__icontains=self.search_term)|
                Q(user__first_name__icontains=self.search_term)|
                Q(user__last_name__icontains=self.search_term)).distinct()
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(LendingList, self).get_context_data(**kwargs)
        if self.search_performed:
            context['search_performed'] = True
            queries_without_page = self.request.GET.copy()
            if queries_without_page.has_key('page'):
                del queries_without_page['page']
            context['queries'] = queries_without_page
            context['search_term'] = self.search_term
        return context


class AddLending(CreateView):
    model = Lending
    template_name = 'lending/add_lending.html'
    form_class = AddLendingForm

    def get_success_url(self):
        return reverse('lending-added', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(AddLending, self).get_form_kwargs()
        self.book = Book.objects.get(pk=self.kwargs['book_pk'])
        kwargs['book'] = self.book
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AddLending, self).get_context_data(**kwargs)
        context['book'] = self.book
        return context


class ViewLending(DetailView):
    model = Lending
    template_name = 'lending/view_lending.html'


class FinishLending(UpdateView):
    model = Lending
    template_name = 'lending/finish_lending.html'
    form_class = FinishLendingForm

    def get_success_url(self):
        return reverse('view-lending', args=[self.object.id])


class EditLending(UpdateView):
    model = Lending
    template_name = 'lending/edit_lending.html'
    form_class = EditLendingForm

    def get_success_url(self):
        return reverse('view-lending', args=[self.object.id])


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
    paginate_by = 5

    def get_queryset(self):
        self.user = User.objects.get(username=self.kwargs['username'])
        return Lending.objects.filter(user=self.user, end_date=None).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersCurrentLendings, self).get_context_data(**kwargs)
        context['lender'] = self.user
        return context


class UsersLendings(ListView):
    model = Lending
    template_name = "lending/users_lendings.html"
    paginate_by = 5

    def get_queryset(self):
        self.user = User.objects.get(username=self.kwargs['username']) 
        return Lending.objects.filter(user=self.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersLendings, self).get_context_data(**kwargs)
        context['lender'] = self.user
        return context


class UsersList(ListView):
    model = User
    template_name = "lending/users.html"
    paginate_by = 10
    queryset = User.objects.order_by('last_name')





