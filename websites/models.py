from django.db import models
from clients.models import ClientProfile

class Website(models.Model):
    """
    A website that belongs to a client and contains multiple pages.
    """
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='websites')
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    """
    A page that belongs to a website and contains multiple content blocks.
    """
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.website.name})"


class ContentBlock(models.Model):
    """
    Content blocks that are placed on a page. They can be text, images, galleries, etc.
    """
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='content_blocks')
    block_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'), 
        ('image', 'Image'),
        ('gallery', 'Gallery'),
        ('video', 'Video Embed'),
        ('contact_form', 'Contact Form'),
        ('custom_html', 'Custom HTML')
    ])
    content = models.TextField(blank=True, null=True)  # Used for text, video URLs, or HTML content
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)  # For single image blocks
    position = models.IntegerField()  # To manage the order of blocks

class GalleryImage(models.Model):
    """
    Gallery images for content blocks that contain multiple images.
    """
    image = models.ImageField(upload_to='uploads/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
