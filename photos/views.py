from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gallery(request):
    return render(request, 'photos/gallery.html')

def viewImage(request):
    return render(request, 'photos/image.html')

def addImage(request):
    return render(request, 'photos/add_image.html')