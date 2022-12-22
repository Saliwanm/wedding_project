from django.urls import path
from .views import articles


urlpatterns = [
    path('', articles, name='articles'),
]