from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateField, DateInput
from .models import Forum, ForumComment


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "enter article's name",
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "the articles description here",
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': "date of publication for example '2022-12-24'",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = ForumComment
        fields = ['full_text', 'cut']