from django.db import models


class About(models.Model):
    """
    Model representing the About page content.
    Includes fields for title, last update time, and main content.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
