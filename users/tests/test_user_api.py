from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserApiTests(APITestCase):

    def test_register_user_with_missing_fields_all(self):
        """Test for validating errors when registering with all required fields missing"""
        url = reverse('user-register')
        data = {
            'username': '',  # Пустое поле для username
            'password': '',  # Пустое поле для password
            'email': '',     # Пустое поле для email
            'phone': '',     # Пустое поле для phone
            'position': '',   # Пустое поле для position
            'project': '',    # Пустое поле для project
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверяем, что указаны все обязательные поля
        self.assertIn("username", response.data)
        self.assertIn("password", response.data)
        self.assertIn("email", response.data)  # Проверяем наличие поля email
        self.assertIn("phone", response.data)
        self.assertIn("position", response.data)
        self.assertIn("project", response.data)

    def test_register_user_with_missing_fields_email(self):
        """Test for validating errors when registering with missing email field"""
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'phone': '1234567890',
            'position': 'Developer',
            'project': 'Project X'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)  # Проверяем, что поле email указано в ответе об ошибке

    def test_register_user_with_missing_fields_password(self):
        """Test for validating errors when registering with missing password field"""
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone': '1234567890',
            'position': 'Developer',
            'project': 'Project X'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)  # Проверяем, что поле password указано в ответе об ошибке

    def test_get_user_details_success(self):
        """Test for successfully retrieving specific user details"""
        user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        url = reverse('user-detail', args=[user.id])  # Используем ID пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)  # Проверяем, что имя пользователя совпадает

    def test_get_user_details_not_found(self):
        """Test for retrieving a user that does not exist, expecting a 404 response"""
        url = reverse('user-detail', args=[999])  # Используем несуществующий ID пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)  # Проверяем наличие ключа detail в ответе
        self.assertEqual(response.data["detail"], "No CustomUser matches the given query.")  # Проверяем конкретное сообщение об ошибке
