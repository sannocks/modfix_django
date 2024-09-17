from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClientProfile

@login_required
def client_dashboard(request):
    profile = request.user.profile
    return render(request, 'clients/client_dashboard.html', {'profile': profile})
