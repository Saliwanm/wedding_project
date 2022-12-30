from django.forms import ModelForm
from django import forms
from .models import PhotoAvatar, UserProfile


class PhotoAvatarForm(ModelForm):
    image = forms.ImageField()

    class Meta:
        model = PhotoAvatar
        fields = ['image']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image_url', 'phone', 'country', 'web_site', 'language', 'price', 'hour']