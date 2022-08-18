from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'accounts/register.html',{})

def login(request):
    return render(request,'accounts/login.html',{})


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