from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from django.contrib.auth.backends import ModelBackend

# Create your models here.


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
