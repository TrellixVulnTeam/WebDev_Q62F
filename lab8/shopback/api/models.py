from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=10)
    description = models.TextField(max_length=1000)
    count = models.IntegerField(default=0)
    rating = models.IntegerField(default=1)
    imageSrc = models.CharField(max_length=500)
    amazonLink = models.CharField(max_length=500)
    prodcategory = models.IntegerField(default=1)
    is_active = models.BooleanField()
    likes = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=300)

