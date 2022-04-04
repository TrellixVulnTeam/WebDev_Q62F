from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=10)
    description = models.TextField(max_length=1000)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=300)

