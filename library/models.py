from django.db import models
import lending

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def full_name(self):
    	return self.first_name + " " + self.last_name

    def __unicode__(self):
    	return self.full_name()

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.name

class Category(models.Model):
	# kategorije mogu biti npr. "Programiranje", "Project management" i sl. 
    name = models.CharField(max_length=20)

    class Meta:
    	verbose_name_plural = "categories"

    def __unicode__(self):
    	return self.name

class Tag(models.Model):
	# tagovi mogu biti npr. "Python", "CSS", "Photoshop", odnosno, konkretniji su od kategorije 
    name = models.CharField(max_length=50)

    def __unicode__(self):
    	return self.name

class Book(models.Model):
    LANGUAGE_CHOICES = (('hr','Croatian'),('eng','English'),('ger','German'))
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    isbn = models.CharField(max_length=24)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_year = models.IntegerField()
    cover_image = models.ImageField(upload_to='cover_images', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    category = models.ForeignKey(Category)

    def __unicode__(self):
    	return self.title

    def get_authors(self):
    	l = ""
    	for author in self.authors.all():
    		l += author.full_name()+", "
    	return l[:-2] 

    get_authors.short_description = 'authors'

    def get_tags(self):
    	l = ""
    	for tag in self.tags.all():
    		l += tag.name +", "
    	return l[:-2]

    get_tags.short_description = 'tags'

    def get_number_of_book_items(self):
    	return lending.models.BookItem.objects.all().filter(book=self).count()

    get_number_of_book_items.short_description = 'total'

    def get_number_of_borrowed_book_items(self):
    	return lending.models.BookItem.objects.all().filter(book=self, borrowed=True).count()

    get_number_of_borrowed_book_items.short_description = 'borrowed'



