from django import forms
from .models import Page, ContentBlock

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'slug']

class ContentBlockForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = ['block_type', 'title', 'text_content', 'image', 'additional_images', 'form_data', 'cta_text', 'cta_link', 'image_with_text', 'image_with_text_content']
