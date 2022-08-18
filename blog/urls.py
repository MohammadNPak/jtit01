
from django.urls import path
from . import views
urlpatterns = [
    path('add-education', views.add_education, name='add-education'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('post', views.post, name='post'),
    path('profiles', views.profiles, name='profiles'),
    path('add-experience', views.add_experience, name='add-experience'),
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('create-profile', views.create_profile, name='create-profile'),
    path('profile', views.profile, name='profile'),

]