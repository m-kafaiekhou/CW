from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.html import mark_safe

# Create your models here.


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.photo.url
        ))
