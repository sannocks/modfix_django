from django.shortcuts import render



def home(request):
    return render(request, 'index/home.html')

def pricing(request):
    return render(request, 'index/pricing.html')

def contact(request):
    return render(request, 'index/contact.html')

def faq(request):
    return render(request, 'index/faq.html')

def privacy_policy(request):
    return render(request, 'index/privacy_policy.html')