from django.urls import path
from .views import forum


urlpatterns = [
    path('', forum, name='forum'),
]