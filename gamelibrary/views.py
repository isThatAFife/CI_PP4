from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings
from django.contrib import messages
from .models import Game
from .forms import CommentForm
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Comment


@login_required
def user_comments(request):
    """
    Display comments made by the logged-in user.

    This view fetches all comments made by the current user, ordered by creation date,
    and renders them in the user_comments.html template.
    """
    user_comments = (
        Comment.objects.filter(author=request.user)
        .select_related("post")
        .order_by("-created_on")
    )
    return render(
        request, "gamelibrary/user_comments.html", {"comments": user_comments}
    )


def get_igdb_access_token(client_id, client_secret):
    """
    Obtain an access token from the IGDB API.

    Args:
        client_id (str): The IGDB client ID.
        client_secret (str): The IGDB client secret.

    Returns:
        str: The access token for IGDB API requests.
    """
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    response = requests.post(url, params=params)
    return response.json()["access_token"]


def igdb_request(endpoint, query, access_token, client_id):
    """
    Make a request to the IGDB API.

    Args:
        endpoint (str): The IGDB API endpoint.
        query (str): The query string for the API request.
        access_token (str): The IGDB API access token.
        client_id (str): The IGDB client ID.

    Returns:
        dict: The JSON response from the IGDB API.
    """
    url = f"https://api.igdb.com/v4/{endpoint}"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    }
    response = requests.post(url, headers=headers, data=query)
    return response.json()


class GameList(generic.ListView):
    """
    A view to display a list of games.

    This view fetches all games from the database, orders them by metascore,
    and displays them in a paginated list. It also fetches cover images for games
    that don't have one stored locally.
    """
    queryset = Game.objects.all().order_by("-metascore")
    template_name = "gamelibrary/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Add cover images to the context data for each game.

        This method fetches cover images from the IGDB API for games that don't have
        a cover URL stored locally.
        """
        context = super().get_context_data(**kwargs)
        games = context["object_list"]

        client_id = settings.IGDB_CLIENT_ID
        client_secret = settings.IGDB_CLIENT_SECRET
        access_token = get_igdb_access_token(client_id, client_secret)

        for game in games:
            if not game.cover_url:
                query = f'fields name,cover.url; where name ~ "{game.name}";'
                igdb_games = igdb_request("games", query, access_token, client_id)
                if igdb_games and "cover" in igdb_games[0]:
                    cover_url = igdb_games[0]["cover"]["url"]
                    high_quality_url = cover_url.replace("t_thumb", "t_cover_big")
                    game.cover_url = high_quality_url
                    game.save()

        return context


def game_detail(request, slug):
    """
    Display details of a specific game and handle comment submissions.

    This view fetches a game by its slug, displays its details, comments, and a form
    for submitting new comments. It also fetches the game's cover image from IGDB if
    it's not already stored locally.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the game to display.

    Returns:
        HttpResponse: The rendered game detail page.
    """
    queryset = Game.objects.all().order_by("-metascore")
    game = get_object_or_404(queryset, slug=slug)
    comments = game.comments.all().order_by("-created_on")
    comment_count = game.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = game
            comment.save()

            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    # Fetch cover from IGDB
    client_id = settings.IGDB_CLIENT_ID
    client_secret = settings.IGDB_CLIENT_SECRET
    access_token = get_igdb_access_token(client_id, client_secret)

    query = f'fields name,cover.url; where name ~ "{game.name}";'
    igdb_games = igdb_request("games", query, access_token, client_id)

    if igdb_games and "cover" in igdb_games[0]:
        cover_url = igdb_games[0]["cover"]["url"]
        high_quality_url = cover_url.replace("t_thumb", "t_cover_big")
        game.cover_url = high_quality_url
        game.save()

    return render(
        request,
        "gamelibrary/game_detail.html",
        {
            "game": game,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
