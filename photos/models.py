from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    categoryx = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories

    def __str__(self):
        return self.categoryx

class Location(models.Model):
    locationx = models.CharField(max_length=25)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id, new_location):
        cls.objects.filter(id = id).update(locationx = new_location)

    def __str__(self):
        return self.locationx

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image_location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self) -> str:
        return self.name
