from django.urls import path
from .views import forum
from . import views


urlpatterns = [
    path('', forum, name='forum'),
    path('<int:id>', views.ForumDetailView, name='forum_detail'),
    path('comment_create/<int:id>', views.comment_crate, name='comment_create'),
    path('forum_create', views.forum_create, name='forum_create'),
]