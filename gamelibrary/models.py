from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class Game(models.Model):

    name = models.CharField(max_length=200, unique=False, null=False)
    metascore = models.IntegerField(default=0)
    console = models.CharField(max_length=200, default="NA")
    userscore = models.CharField(max_length=3, default="0")
    date = models.CharField(max_length=100, default="1998")
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    cover_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Combine name and console, then slugify
            slug_str = f"{self.name} {self.console}"
            self.slug = slugify(slug_str)

            # Ensure uniqueness of the slug
            original_slug = self.slug
            count = 1
            while Game.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1

        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`gamelibrary.Game`.
    """

    post = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
