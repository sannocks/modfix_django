from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, pricing, contact, faq, privacy_policy

urlpatterns = [
    path('', home, name='home'),
    path('pricing/', pricing, name='pricing'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
]
