# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
