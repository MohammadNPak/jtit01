
from django.urls import path
from . import views
urlpatterns = [
    
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('add-education', views.add_education, name='add-education'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profiles', views.profiles, name='profiles'),
    path('add-experience', views.add_experience, name='add-experience'),
    path('create-profile', views.create_profile, name='create-profile'),
    path('profile', views.profile, name='profile'),
]