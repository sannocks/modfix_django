from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['content_block', 'staff_member', 'status', 'urgency', 'time_spent', 'created_at']
    list_filter = ['status', 'urgency', 'created_at']
    search_fields = ['client__user__username', 'content_block__page__title']
