from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    name = models.CharField(max_length=48)
    description = models.CharField(max_length= 100)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    categoryx = models.CharField(max_length=18)

    def __str__(self):
        return self.categoryx

class Location(models.Model):
    locationx = models.CharField(max_length=25)

    def __str__(self):
        return self.locationx
