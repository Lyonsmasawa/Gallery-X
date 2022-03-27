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

    @classmethod
    def get_category_by_id(cls, id):
        category = cls.objects.get(id = id)
        return category

    def __str__(self):
        return self.categoryx

class Location(models.Model):
    locationx = models.CharField(max_length=25)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_all_locations(cls):
        locations = cls.objects.all()
        return locations

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

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def get_images_by_category(cls, category):
        images = cls.objects.filter(image_category__categoryx = category)
        return images

    @classmethod
    def get_images_by_location(cls, location):
        images = cls.objects.filter(image_location__locationx = location)
        return images
    
    

    def __str__(self) -> str:
        return self.name
