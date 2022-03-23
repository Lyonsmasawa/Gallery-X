from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    categoryx = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryx

class Location(models.Model):
    locationx = models.CharField(max_length=25)    

    def __str__(self):
        return self.locationx

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length= 100)
    post_date = models.DateTimeField(auto_now_add=True)
    image_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image_location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)

    def save_image(self):
        self.save()

    def __str__(self) -> str:
        return self.name
