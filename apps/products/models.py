from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    date_create = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publicated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
