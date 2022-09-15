
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def register(request):
    return render(request,'accounts/register.html',{})

def login(request):
    if request.method == "GET":
        return render(request,'accounts/login.html',{})
    elif request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect(reverse("dashboard"))
        messages.add_message(request,messages.ERROR,f"username or password is invalid")
        return  render(request,'accounts/login.html',{})



def add_education(request):
    return render(request,'accounts/add-education.html',{})

def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def add_experience(request):
    return render(request,'accounts/add-experience.html',{})


def create_profile(request):
    return render(request,'accounts/create-profile.html',{})



def profile(request):
    person = {
        'username':"mohamadnpak",
        'bio':"I'm jango developer",
        'first_name':'mohammad',
        'last_name':'nozari pak',
        'skills':[
            'html',
            'css',
            'js',
            'python',
            'jango'
        ]
    }
    username = "mohammadnpak"
    return render(request,'accounts/profile.html',{'person':person})