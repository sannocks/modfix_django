from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Website, Page, ContentBlock

@login_required
def website_list(request):
    websites = Website.objects.filter(client=request.user.profile)
    return render(request, 'websites/website_list.html', {'websites': websites})

@login_required
def page_list(request, website_id):
    website = get_object_or_404(Website, id=website_id, client=request.user.profile)
    pages = website.pages.all()
    return render(request, 'websites/page_list.html', {'website': website, 'pages': pages})
