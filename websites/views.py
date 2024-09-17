from django.shortcuts import render, get_object_or_404, redirect
from .models import Website, Page
from .forms import PageForm, WebsiteForm
from django.contrib.auth.decorators import login_required

@login_required
def page_list(request):
    pages = Page.objects.filter(website__client=request.user)
    return render(request, 'websites/page_list.html', {'pages': pages})

@login_required
def create_page(request):
    website, created = Website.objects.get_or_create(client=request.user)
    
    if created:
        # If a new website was created, redirect to a setup page or a message indicating that setup is complete
        return redirect('website_setup')  # Define this URL to handle new website setup

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.website = website
            page.save()
            return redirect('page_list')
    else:
        form = PageForm()

    return render(request, 'websites/page_form.html', {'form': form})


@login_required
def website_setup(request):
    website, created = Website.objects.get_or_create(client=request.user)

    if request.method == 'POST':
        form = WebsiteForm(request.POST, instance=website)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = WebsiteForm(instance=website)

    return render(request, 'websites/website_setup.html', {'form': form})

