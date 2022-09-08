from django.shortcuts import render
from datetime import datetime
# Create your views here.
from .models import Post

def posts(request):
    p = Post.objects.all()
    return render(request,'blog/posts.html',{'posts':p})

def index(request):
    return render(request,'blog/index.html',{})

def post(request):
    return render(request,'blog/post.html',{})

