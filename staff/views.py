from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse

# Check if the user is either a superuser or has staff status
def staff_check(user):
    return user.is_superuser or user.is_staff

# Redirect unauthenticated users to the login page
@user_passes_test(staff_check, login_url='account_login')  # 'account_login' is the default login URL from allauth
def staff_dashboard(request):
    return render(request, 'staff/dashboard.html')
