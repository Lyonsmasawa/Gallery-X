from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from .models import Category, Location, Image

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category is None:
        images = Image.get_all_images()   
    else:
        images = Image.get_images_by_category(category)
    
    categories = Category.get_all_categories()    

    context = {'categories': categories, 'images': images}
    return render(request, 'photos/gallery.html', context)

def viewImage(request, id):

    image = Image.get_image_by_id(id)

    context = {'image': image}
    return render(request, 'photos/image.html', context)

def addImage(request):

    categories = Category.get_all_categories()

    # if request.method == 'POST':
    #     data = request.POST
    #     uploaded_image = request.FILES.get('image')

        # print('data:',data) test if data gets through
        # print('image:',image)

        # if data['category'] is not None:
        #     category = Category.get_category_by_id(data['category'])
        # elif data['add_category'] is not None:
        #     category, created = Category.objects.get_or_create(categoryx = data['add_category'])
        # else: 
        #     category = None

        # image = Image.objects.create(
        #     image = uploaded_image
        #     name = data['name']
        #     description = data['description']
        #     image_location = data['location']
        #     image_category = category
        # )

        # return redirect('gallery')

    context = {'categories': categories,}
    return render(request, 'photos/add_image.html', context)