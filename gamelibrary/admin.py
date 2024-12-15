from django.contrib import admin
from .models import Game, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    """
    Admin class for the Game model.
    Customizes the admin interface with list display, search, filtering, and Summernote integration.
    """

    list_display = ("name", "console", "metascore", "date")
    search_fields = ["name"]
    list_filter = ("date", "metascore")
    prepopulated_fields = {"name": ("metascore",)}
    summernote_fields = ("content",)


admin.site.register(Comment)
