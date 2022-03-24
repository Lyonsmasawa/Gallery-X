from django.contrib import admin

# Register your models here.
from .models import Image, Category, Location

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)