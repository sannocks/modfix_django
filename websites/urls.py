from django.urls import path
from .views import website_list, page_list

urlpatterns = [
    path('', website_list, name='website_list'),
    path('<int:website_id>/pages/', page_list, name='page_list'),
]
