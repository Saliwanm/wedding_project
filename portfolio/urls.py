from django.urls import path
from .views import portfolio
from . import views


urlpatterns = [
    path('', views.upload, name='portfolio'),
    path('<int:movie_id>', views.movie, name='portfolio'),
]