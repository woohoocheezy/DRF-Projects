from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True) # the ID of book
    title = models.CharField(max_length=50) # the title of book
    author = models.CharField(max_length=50) # the author of book
    category = models.CharField(max_length=50) # the category of book
    pages = models.IntegerField() # the number of pages in book
    price = models.IntegerField() # the price of book
    published_date = models.DateField() # the published date of book
    description = models.TextField() # the description of book