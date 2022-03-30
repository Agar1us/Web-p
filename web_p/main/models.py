from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Post(models.Model):

    header = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header

class Comment(models.Model):

    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
