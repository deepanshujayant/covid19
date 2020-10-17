from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Corona(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
