from django.db import models
from datetime import datetime
from products.models import Product
from .account import Account

class Purchase(models.Model):
    hour = models.DateTimeField(default=datetime.today())
    items = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self) -> str:
        items_and_amount = f'{self.items} - {self.amount}'
        return items_and_amount
