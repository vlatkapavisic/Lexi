from django.db import models
import library

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def full_name(self):
    	return self.first_name + " " + self.last_name

    def __unicode__(self):
    	return self.full_name()

class BookItem(models.Model):
    book = models.ForeignKey(library.models.Book)
    borrowed = models.BooleanField(default=False)
    item_id = models.IntegerField(default=1)

    def __unicode__(self):
      return self.book.title

    def book_title(self):
      return self.book.title

    def get_borrower(self):
      if self.borrowed:
        return Lending.objects.get(book_item=self).user.full_name()
      else:
        return ""

    get_borrower.short_description = 'borrowed by'

    class Meta:
      unique_together = ("book","item_id")
      ordering = ['book']


class Lending(models.Model):
    book_item = models.ForeignKey(BookItem, limit_choices_to={'borrowed': False})
    user = models.ForeignKey(User)
    start_date = models.DateField() 
    end_date = models.DateField(blank=True, null=True) 

    def book_title(self):
      return self.book_item.book_title()

    def user_name(self):
      return self.user.full_name()

   


   


