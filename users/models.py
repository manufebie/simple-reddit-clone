from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/avatars', default='users/avatars/default.png')

    def __str__(self):
        return self.user
