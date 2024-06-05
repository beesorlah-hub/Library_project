from django.db import models
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import DateField
# from rest_framework.settings import api_settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, default="unknown Author")
    biography = models.CharField(max_length=1000, default="")
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    # def __str__(self):
    #     return self.name()

class Publisher(models.Model):
    name = models.CharField(max_length=300, default="unknown Publisher")
    address= models.CharField(max_length=50, default="")
    website = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name()


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn= models.CharField(max_length=50, default="")
    publication_date = models.DateField(auto_now= True)
    page_count =  models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE, default=1)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=1)



    # def __str__(self):
    #     return self.title()
#

class Borrower(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Loan(models.Model):
    loan_date = models.DateField()
    return_date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.loan_date} {self.return_date}'



    
    
