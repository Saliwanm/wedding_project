from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class PhotoAvatar(models.Model):
    image = models.ImageField(upload_to='main/files/covers')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class UserProfile(models.Model):
    image_url = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    country = models.CharField(max_length=255, blank=True)
    web_site = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=10, blank=True)
    hour = models.CharField(max_length=10, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone