from django.contrib import admin
from .models import ClientProfile, Plan

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'available_hours']
    search_fields = ['user__username', 'plan__name']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'monthly_hours']
    search_fields = ['name']
