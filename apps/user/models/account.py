from django.db import models
from .client import Client
from .purchase import Purchase

class Account(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='Client repective')
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, blank=True)

    def __str__(self) -> str:
        return self.client
