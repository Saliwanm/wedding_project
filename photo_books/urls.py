from django.urls import path
from .views import photo_books


urlpatterns = [
    path('', photo_books, name='photo_books'),
]