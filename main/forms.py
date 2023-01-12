from django.forms import ModelForm
from django import forms
from .models import PhotoAvatar, UserProfile


class PhotoAvatarForm(ModelForm):
    image = forms.ImageField()
    user = forms.TextInput()

    class Meta:
        model = PhotoAvatar
        fields = ['image', 'user']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image_url', 'phone', 'country', 'web_site', 'language', 'price', 'hour']