from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.email
