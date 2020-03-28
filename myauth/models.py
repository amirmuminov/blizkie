from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    is_sitter = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    objects = CustomUserManager()



