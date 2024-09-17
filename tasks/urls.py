from django.urls import path
from .views import task_list, update_task_status

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:task_id>/update/', update_task_status, name='update_task_status'),
]
