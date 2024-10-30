# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django admin interface
    path('users/', include('users.urls')),  # Include URLs from the 'users' app for user-related endpoints
]
