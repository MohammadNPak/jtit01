from django.shortcuts import render
from datetime import datetime
# Create your views here.
from .models import Post

def posts(request):
    p1 = Post('post1',datetime.now(),'post1 body','mohammadnpak')
    p2 = Post('post2',datetime.now(),'post2 body','mohammadnpak')

    p = {"p1":p1,"p2":p2}
    return render(request,'blog/posts.html',{'posts':p})

def index(request):
    return render(request,'blog/index.html',{})

def post(request):
    return render(request,'blog/post.html',{})

