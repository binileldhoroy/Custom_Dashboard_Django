import email
from email.policy import default
from django.db import models

# Create your models here.



class BaseUser(models.Model):
    username = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True)

class Ebook(models.Model):
    book = models.CharField(max_length=150,null=True)
    author = models.CharField(max_length=150,null=True)
    price = models.IntegerField()
    image = models.ImageField(null=True,default='')