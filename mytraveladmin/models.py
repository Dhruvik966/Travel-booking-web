from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)


class Packages(models.Model):
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=200)
    title  = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    days = models.IntegerField()
    nights = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='pakage_pics')

    def __str__(self):
        return self.name
    

