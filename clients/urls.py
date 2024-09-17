from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

]
from django.urls import path
from .views import client_dashboard

urlpatterns = [
    path('dashboard/', client_dashboard, name='client_dashboard'),
]
