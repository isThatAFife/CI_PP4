from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Game(models.Model):
    """
    Represents a video game in the game library.

    This model stores information about individual games, including their name,
    scores, console, release date, and cover image URL.
    """

    name = models.CharField(max_length=200, unique=False, null=False)
    metascore = models.IntegerField(default=0)
    console = models.CharField(max_length=200, default="NA")
    userscore = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.CharField(max_length=100, default="1998")
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    cover_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Custom save method to generate a unique slug for each game.

        The slug is created by combining the game's name and console.
        If a slug already exists, a number is appended to ensure uniqueness.
        """
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
    Represents a user comment on a game.

    This model stores individual comments related to a specific game and user,
    including the comment body, approval status, and creation timestamp.
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
