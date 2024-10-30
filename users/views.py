from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer, UserDetailSerializer, UserRegisterSerializer  # Импортируем сериализаторы

User = get_user_model()  # Получаем пользовательскую модель

class UserListGenericView(ListCreateAPIView):
    queryset = User.objects.all()  # Получаем всех пользователей
    serializer_class = UserListSerializer  # Указываем сериализатор для списка пользователей

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()  # Получаем всех пользователей для представления деталей
    serializer_class = UserDetailSerializer  # Указываем сериализатор для деталей пользователя

class RegisterUserGenericView(CreateAPIView):
    queryset = User.objects.all()  # Получаем всех пользователей для регистрации
    serializer_class = UserRegisterSerializer  # Используем сериализатор для регистрации








