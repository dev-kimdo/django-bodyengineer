from tkinter import CASCADE
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField()

    # author = models.CharField(max_length=100)

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.title} | {self.body}'
        else:
            return f'{self.body}'