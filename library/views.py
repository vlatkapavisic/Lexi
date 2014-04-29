# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, FormView, TemplateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView
from library.forms import BookSearchForm
from lending.forms import AddLendingToSelfForm, AddLendingForm
from library.models import *
from lending.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator




class Home(TemplateView):
    template_name = 'lexi.html'


class Readme(TemplateView):
    template_name = 'library/readme.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Readme, self).dispatch(request, *args, **kwargs)


class TagsList(ListView):
    model = Tag
    paginate_by = 10
    template_name = "library/tags.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TagsList, self).dispatch(request, *args, **kwargs)


class CategoriesList(ListView):
    model = Category
    paginate_by = 10
    template_name = "library/categories.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesList, self).dispatch(request, *args, **kwargs)


class BookList(ListView):
    model = Book
    paginate_by = 3
    template_name = "library/books.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Book.objects.all()
        self.search_performed = False
        self.search_term = self.request.GET.get('search')
        if self.search_term:
            self.search_performed = True
            return queryset.filter(Q(title__icontains=self.search_term)|
                Q(description__icontains=self.search_term)|
                Q(authors__first_name__icontains=self.search_term)|
                Q(authors__last_name__icontains=self.search_term)|
                Q(publisher__name__icontains=self.search_term)|
                Q(tags__name__icontains=self.search_term)|
                Q(category__name__icontains=self.search_term)).distinct()
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        if self.search_performed:
            context['search_performed'] = True
            queries_without_page = self.request.GET.copy()
            if queries_without_page.has_key('page'):
                del queries_without_page['page']
            context['queries'] = queries_without_page
            context['search_term'] = self.search_term
        return context


class BookDetailAndLend(CreateView):
    model = Lending
    template_name = 'library/book_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookDetailAndLend, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('lending-added', args=[self.object.id])

    def get_form_class(self):
        if self.request.user.has_perm('lending.add_lending'):
            form_class = AddLendingForm
        else:
            form_class = AddLendingToSelfForm
        return form_class

    def get_form_kwargs(self):
        kwargs = super(BookDetailAndLend, self).get_form_kwargs()
        self.book = Book.objects.get(pk=self.kwargs['pk'])
        kwargs['book'] = self.book
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(BookDetailAndLend, self).get_context_data(**kwargs)
        context['book'] = self.book
        return context


class AuthorsBooks(ListView):
    model = Book
    template_name = "library/authors_books.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorsBooks, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.author = get_object_or_404(Author, pk=self.kwargs['pk'])
        return Author.objects.get(pk=self.kwargs['pk']).books.all(). \
            order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AuthorsBooks, self).get_context_data(**kwargs)
        context['author'] = self.author
        return context


class PublishersBooks(ListView):
    model = Book
    template_name = "library/publishers_books.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PublishersBooks, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, pk=self.kwargs['pk'])
        return Book.objects.filter(publisher=self.publisher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PublishersBooks, self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context


class TagsBooks(ListView):
    model = Book
    template_name = "library/tags_books.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TagsBooks, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Book.objects.filter(tags__name=self.tag).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(TagsBooks, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class CategorysBooks(ListView):
    model = Book
    template_name = "library/categorys_books.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategorysBooks, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Book.objects.filter(category__name=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategorysBooks, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class AdvancedSearch(ListView):
    model = Book
    template_name = "library/advanced_search.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvancedSearch, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.search_performed = False
        for search_term in self.request.GET.values():
            if search_term != "":
                self.search_performed = True

        filters = Q()

        self.title = self.request.GET.get('title')
        if self.title:
            filters &= Q(title__icontains=self.title)

        self.authors = self.request.GET.get('authors')
        if self.authors:
            authors_names = self.authors.split(', ')
            for name in authors_names:
                filters |= Q(authors__name__icontains=name)

        self.publisher = self.request.GET.get('publisher')
        if self.publisher:
            filters &= Q(publisher__name__icontains=self.publisher)

        self.tags = self.request.GET.get('tags')
        if self.tags:
            tags_list = self.tags.split(', ')
            for tag in tags_list:
                filters |= Q(tags__name__icontains=tag)

        self.category = self.request.GET.get('category')
        if self.category:
            filters &= Q(category__name__icontains=self.category)

        if self.search_performed:
            queryset = Book.objects.filter(filters).distinct().order_by('-id')
        else:
            queryset = []
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AdvancedSearch, self).get_context_data(**kwargs)
        if self.search_performed:
            context['search_performed'] = True
            queries_without_page = self.request.GET.copy()
            if queries_without_page.has_key('page'):
                del queries_without_page['page']
            context['queries'] = queries_without_page
        return context


