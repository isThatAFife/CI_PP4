from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(max_length=100,unique=False)
    score = models.DecimalField(max_digits=2, decimal_places=1)
    year = models.PositiveIntegerField(default=1997, validators=[MinValueValidator(1920), MaxValueValidator((datetime.date.today().year+1))])
    developer = models.CharField(max_length=200, unique=False)
    publisher = models.CharField(max_length=200, unique=False)