from django.db import models
from .client import Client

class Account(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='Client')

    def __str__(self) -> str:
        return self.client.first_name
