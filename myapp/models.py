from django.db import models

# Create your models here.


class Databases(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=20, unique=True)
    message = models.TextField(max_length=500)

    def __str__(self):
       return self.name 