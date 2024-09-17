from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import page_list, create_page, website_setup

urlpatterns = [
    path('pages/', page_list, name='page_list'),
    path('pages/new/', create_page, name='create_page'),
    path('website/setup/', website_setup, name='website_setup'), 
]
