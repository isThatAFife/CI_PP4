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
    user_comments = Comment.objects.filter(author=request.user).select_related('post').order_by('-created_on')
    return render(request, 'gamelibrary/user_comments.html', {'comments': user_comments})


def get_igdb_access_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    return response.json()["access_token"]


def igdb_request(endpoint, query, access_token, client_id):
    url = f"https://api.igdb.com/v4/{endpoint}"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }
    response = requests.post(url, headers=headers, data=query)
    return response.json()


class GameList(generic.ListView):
    queryset = Game.objects.all().order_by('-metascore')
    template_name = "gamelibrary/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = context['object_list']

        # Fetch covers for all games
        client_id = settings.IGDB_CLIENT_ID
        client_secret = settings.IGDB_CLIENT_SECRET
        access_token = get_igdb_access_token(client_id, client_secret)

        for game in games:
            if not game.cover_url:
                query = f'fields name,cover.url; where name ~ "{game.name}";'
                igdb_games = igdb_request(
                    "games", query, access_token, client_id)
                if igdb_games and 'cover' in igdb_games[0]:
                    cover_url = igdb_games[0]['cover']['url']
                    high_quality_url = cover_url.replace(
                        't_thumb', 't_cover_big')
                    game.cover_url = high_quality_url
                    game.save()

        return context


def game_detail(request, slug):
    queryset = Game.objects.all().order_by('-metascore')
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
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
        
    comment_form = CommentForm()

    # Fetch cover from IGDB
    client_id = settings.IGDB_CLIENT_ID
    client_secret = settings.IGDB_CLIENT_SECRET
    access_token = get_igdb_access_token(client_id, client_secret)

    query = f'fields name,cover.url; where name ~ "{game.name}";'
    igdb_games = igdb_request("games", query, access_token, client_id)

    if igdb_games and 'cover' in igdb_games[0]:
        cover_url = igdb_games[0]['cover']['url']
        high_quality_url = cover_url.replace('t_thumb', 't_cover_big')
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
