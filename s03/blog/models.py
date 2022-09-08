from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author =models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.author.user.username}"



