from django.urls import path
from .views import UserDetailView, UserListGenericView, RegisterUserGenericView  # Importing other views

urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/register/', RegisterUserGenericView.as_view(), name='user-register'),  # Endpoint for user registration
]







