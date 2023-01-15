from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('items', views.item_list, name='item-list')

]