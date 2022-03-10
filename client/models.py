from django.db import models
from django.contrib.auth.models import AbstractUser
from config.helpers import UploadTo
from django.conf import settings
import os


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo("profile"))

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url
        return os.path.join(settings.STATIC_URL, 'img/no_avatar.jpg')

