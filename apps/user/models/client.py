from django.contrib.auth.models import User
from django.db import models

class Client(User):
    image = models.ImageField(upload_to='%Y/%m/%d/')

    def __str__(self) -> str:
        return self.first_name
