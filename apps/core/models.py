from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=99999999999)
    message = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.email
