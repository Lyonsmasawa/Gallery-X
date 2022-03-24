from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Category, Location, Image

# Create your views here.
def gallery(request):

    categories = Category.get_all_categories()
    images = Image.get_all_images()

    context = {'categories': categories, 'images': images}
    return render(request, 'photos/gallery.html', context)

def viewImage(request, pk):

    image = Image.get_images_by_id(pk)

    context = {'image': image}
    return render(request, 'photos/image.html', context)

def addImage(request):
    return render(request, 'photos/add_image.html')