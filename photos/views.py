from django.shortcuts import render, redirect
import numpy as np
from django.http import HttpResponse
from django.template import context
from .models import Category, Location, Image

# Create your views here.
def gallery(request):
    location = request.GET.get('location')
    if location is None:
        images = Image.get_all_images()   
    else:
        images = Image.get_images_by_location(location)
    
    categories = Category.get_all_categories() 
    locations = Location.get_all_locations()
    imageArr = np.array(images)
    splitImageArr = np.array_split(imageArr, 3)

    rowOne = splitImageArr[0]
    rowTwo = splitImageArr[1]
    rowThree = splitImageArr[2]

    context = {'categories': categories, 'locations': locations, 'images': images, 'rowOne': rowOne, 'rowTwo': rowTwo, 'rowThree': rowThree,}
    return render(request, 'photos/gallery.html', context)

def viewImage(request, id):

    image = Image.get_image_by_id(id)

    context = {'image': image}
    return render(request, 'photos/image.html', context)


def addImage(request):

    categories = Category.get_all_categories()
    locations = Location.get_all_locations()

    if request.method == 'POST':
        data = request.POST
        uploaded_image = request.FILES.get('image')

        print('data:',data) #test if data gets through
        print('image:',uploaded_image)

        if data['category'] != 'none':
            category = Category.get_category_by_id(data['category'])
            
        elif data['add_category'] != 'none':
            category, created = Category.objects.get_or_create(categoryx = data['add_category'])
        else: 
            category = None

        if data['location'] != 'none':
            location =  Location.get_location_by_id(data['location'])
            
        elif data['add_location'] != 'none':
            location, created = Location.objects.get_or_create(locationx = data['add_location'])
        else: 
            location = None

        image = Image.objects.create(
            image = uploaded_image,
            name = data['name'],
            description = data['description'],
            image_location = location,
            image_category = category,
        )

        return redirect('gallery')

    context = {'categories': categories, 'locations': locations,}
    return render(request, 'photos/add_image.html', context)

def searchImage(request):

    category = request.GET.get('category')

    if category is None:
        message = "You haven't searched for any category"
        return render(request, 'photos/search.html', {"message":message})
    else:
        images = Image.get_images_by_category(category)
        message = f'{category}'

    context = {'images': images, 'message': message, }
    return render(request, 'photos/search.html', context)

def searchImageByLocation(request, id):
    
    location = request.GET.get(id = id)

    if location is None:
        return redirect('gallery')
    else:
        images = Image.get_images_by_location(location)
        message = f'{location}'

    context = {'images': images, 'message': message, }
    return render(request, 'photos/search.html', context)