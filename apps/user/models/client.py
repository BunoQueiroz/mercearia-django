from django.contrib.auth.models import User
from django.db import models

class Client(User):
    image = models.ImageField(upload_to='clients/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.first_name
