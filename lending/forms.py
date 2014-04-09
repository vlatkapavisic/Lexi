from django.forms import ModelForm, DateInput
from django.forms.extras.widgets import SelectDateWidget
from lending.models import Lending, BookItem
from datetime import date
from django.utils.translation import ugettext as _

class LendingForm(ModelForm):
    class Meta:
        model = Lending
        fields = ['user', 'book_item', 'start_date']
        widgets = {
            'start_date': SelectDateWidget
        }

    # def __init__(self, *args, **kwargs):
    #     print kwargs
    #     super(LendingForm, self).__init__(*args, **kwargs)
    #     self.fields['book_item'].queryset = BookItem.objects.filter(
    #         book=kwargs['book'], borrowed=False)


