from django.shortcuts import render
from django.views import generic
from .models import Game

# Create your views here.
class GameList(generic.ListView):
    queryset = Game.objects.all()
    template_name = "game_list.html"

