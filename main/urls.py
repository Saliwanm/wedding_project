from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout_view, name='logout'),
    path('update/<int:id>', views.update_user, name='update_user'),
    path('change_password/<int:id>', views.change_password, name='change_password'),
    path('profile/<int:id>', views.profile, name='profile'),
]