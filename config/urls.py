from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth routes
    path('staff/', include('staff.urls')),
    path('websites/', include('websites.urls')),
    path('', include('index.urls')),
    path('tasks/', include('tasks.urls')),
    path('clients/', include('clients.urls')),
    path('billing/', include('billing.urls')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
