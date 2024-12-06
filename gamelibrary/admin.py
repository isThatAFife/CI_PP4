from django.contrib import admin
from .models import Game
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'year')
    search_fields = ['title']
    list_filter = ('year',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
