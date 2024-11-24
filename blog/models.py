from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="posts")


class Commentary(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="commentaries")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="commentaries")