from django.db import models
from datetime import datetime
from products.models import Product

class Purchase(models.Model):
    hour = models.DateTimeField(default=datetime.now())
    items = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()

    def __str__(self) -> str:
        hour_and_items = f'{self.hour} - {self.items}'
        return hour_and_items
