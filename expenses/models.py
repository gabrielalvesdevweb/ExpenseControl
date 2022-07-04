from ctypes import sizeof
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description
