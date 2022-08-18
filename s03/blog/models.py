from django.db import models

# Create your models here.


class Post:
    def __init__(self,title,date,body,author,) -> None:
        self.title = title
        self.date=date
        self.body = body
        self.author=author

