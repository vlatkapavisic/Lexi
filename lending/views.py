from django.views.generic import ListView
from django.views.generic.detail import DetailView
from lending.models import *


class BookItemList(ListView):
    model = BookItem


class LendingList(ListView):
    model = Lending
    template_name = 'lending/lendings.html'

    def get_queryset(self):
        return Lending.objects.filter(end_date=None)


class LendingDetailView(DetailView):
    model = Lending
