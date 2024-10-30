from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'position', 'project']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone', 'position', 'project']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}  # Убедитесь, что email обязательно
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            position=validated_data['position'],
            project=validated_data['project']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if User.objects.filter(username=attrs.get('username')).exists():
            raise ValidationError({"username": "Пользователь с таким именем уже существует."})

        if User.objects.filter(email=attrs.get('email')).exists():
            raise ValidationError({"email": "Пользователь с такой электронной почтой уже существует."})

        return attrs
