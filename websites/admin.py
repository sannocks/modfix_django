from django.contrib import admin
from .models import Website, Page, ContentBlock, GalleryImage

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'client']
    search_fields = ['name', 'client__user__username']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'website']
    search_fields = ['title', 'website__name']

@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ['block_type', 'page', 'position']
    search_fields = ['page__title', 'block_type']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt_text']
    search_fields = ['alt_text']
