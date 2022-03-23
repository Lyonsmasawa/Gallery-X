from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('', views.gallery, name = 'gallery'),
    re_path('image/<str:pk>/', views.viewImage, name='image'),
    re_path('add/', views.addImage, name = 'add')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)