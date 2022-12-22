from django.urls import path
from .views import photographers


urlpatterns = [
    path('', photographers, name='photographers'),
]