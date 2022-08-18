
from django.urls import path
from . import views
urlpatterns = [
    path('post', views.post, name='post'),
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),

]