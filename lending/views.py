from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, TemplateView, CreateView
from django.views.generic.detail import DetailView
from lending.models import *
from library.models import *
from lending.forms import LendingForm
from django.core.urlresolvers import reverse
from django.utils import timezone



class LendingList(ListView):
    model = Lending
    template_name = 'lending/lendings.html'
    paginate_by = 10

    def get_queryset(self):
        return Lending.objects.order_by('-id')


class NewLending(CreateView):
    model = Lending
    template_name = 'lending/new_lending.html'
    form_class = LendingForm

    def get_success_url(self):
        return reverse('lending-added', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(NewLending, self).get_form_kwargs()
        kwargs.update({'instance': self.object})
        self.book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        kwargs['initial'] = {
            'book_item': BookItem.objects.filter(book=self.book, borrowed=False).first(),
            'start_date': timezone.now()
            }
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(NewLending, self).get_context_data(**kwargs)
        context['book'] = self.book
        return context


class LendingAdded(TemplateView):
    template_name = "lending/lending_added.html"

    def get_context_data(self, **kwargs):
        context = super(LendingAdded, self).get_context_data(**kwargs)
        self.lending = get_object_or_404(Lending, pk=self.kwargs['lending_pk'])
        context['book_title'] = self.lending.book_title()
        context['username'] = self.lending.user_name()
        return context


class UsersCurrentLendings(ListView):
    model = Lending
    template_name = "lending/users_current_lendings.html"
    paginate_by = 3

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Lending.objects.filter(user=self.user, end_date=None).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersCurrentLendings, self).get_context_data(**kwargs)
        context['username'] = self.user.username
        return context


class UsersLendings(ListView):
    model = Lending
    template_name = "lending/users_lendings.html"
    paginate_by = 3

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Lending.objects.filter(user=self.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UsersLendings, self).get_context_data(**kwargs)
        context['username'] = self.user.username
        return context


class UsersList(ListView):
    model = User
    template_name = "lending/users.html"
    paginate_by = 10

