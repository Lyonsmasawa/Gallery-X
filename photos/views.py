from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Category, Location, Image

# Create your views here.
def gallery(request):

    categories = Category.get_all_categories()
    context = {'categories': categories}
    return render(request, 'photos/gallery.html', context)

def viewImage(request, pk):
    return render(request, 'photos/image.html')

def addImage(request):
    return render(request, 'photos/add_image.html')