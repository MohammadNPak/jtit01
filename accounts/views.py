from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'accounts/register.html',{})

def login(request):
    return render(request,'accounts/login.html',{})
