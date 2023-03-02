from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="unnamed", max_length=50)
    date = models.DateTimeField( auto_now=True, auto_now_add=False)
    content = models.CharField( max_length=2000)