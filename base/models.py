import email
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=200)