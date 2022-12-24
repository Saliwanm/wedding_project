from django.forms import ModelForm
from .models import Movie
from django import forms


class MovieForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = Movie
        fields = ['name', 'image']
