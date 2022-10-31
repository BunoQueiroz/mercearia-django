from django.db import models

class People(models.Model):
    username = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name
