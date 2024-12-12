from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game

# Create your views here.
class GameList(generic.ListView):
    queryset = Game.objects.all()
    template_name = "gamelibrary/index.html"
    paginate_by = 6


def game_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "gamelibrary/game_detail.html",
        {"game": game},
    )
