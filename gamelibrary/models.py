from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    
    name = models.CharField(max_length=200, unique=False, null=False)
    metascore = models.IntegerField(default=0)
    console = models.CharField(max_length=200, default='NA')
    userscore = models.CharField(max_length=3, default='0')
    date = models.CharField(max_length=100, default='1998')
 
    