from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Website(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    domain = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    website = models.ForeignKey(Website, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContentBlock(models.Model):
    BLOCK_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('multiple_images', 'Multiple Images'),
        ('form', 'Form'),
        ('cta', 'Call to Action'),
        ('image_text', 'Image with Text'),
    )

    page = models.ForeignKey(Page, related_name='content_blocks', on_delete=models.CASCADE)
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    title = models.CharField(max_length=255, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    additional_images = models.ManyToManyField('AdditionalImage', blank=True)
    form_data = models.JSONField(blank=True, null=True)
    cta_text = models.CharField(max_length=255, blank=True, null=True)
    cta_link = models.URLField(blank=True, null=True)
    image_with_text = models.ImageField(upload_to='images/', blank=True, null=True)
    image_with_text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.get_block_type_display()} - {self.title}'

class AdditionalImage(models.Model):
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f'Image {self.id}'
