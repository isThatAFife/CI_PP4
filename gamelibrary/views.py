from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.conf import settings
from django.contrib import messages
from .models import Game, Comment
from .forms import CommentForm, GameForm
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy

# View for all user comments


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


# View for full list of games


class GameList(generic.ListView):
    """
    A view to display a list of games.

    This view fetches all games from the database, orders them by metascore,
    and displays them in a paginated list. It also fetches cover images for games
    that don't have one stored locally.
    """

    queryset = Game.objects.all().order_by("-metascore")
    template_name = "gamelibrary/index.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """
        Add cover images to the context data for each game.

        This method fetches cover images from the IGDB API for games that don't have
        a cover URL stored locally.
        """
        context = super().get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_superuser
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


# View for game detail page


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

    context = {
        "game": game,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "is_admin": request.user.is_superuser,
    }
    return render(request, "gamelibrary/game_detail.html", context)


# View to edit comments

@login_required
def comment_edit(request, slug, comment_id):
    print("comment edit method called")
    """
    Edit an existing comment on a game post.

    This view handles both GET and POST requests. For POST requests, it updates
    the comment if the form is valid and the user is the author of the comment.
    The comment's approval status is reset to False after editing.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the game post.
        comment_id (int): The ID of the comment to be edited.

    Returns:
        HttpResponseRedirect: Redirects to the game detail page after processing.

    Messages:
        SUCCESS: If the comment is successfully updated.
        ERROR: If there's an error updating the comment.
    """
    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    comments = game.comments.all().order_by("-created_on")
    comment_count = comments.filter(approved=True).count()

    # Fetch the specific comment to edit
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        # Handle form submission for editing
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            updated_comment = comment_form.save(commit=False)
            updated_comment.post = game
            updated_comment.approved = False  # Reset approval after editing
            updated_comment.save()
            messages.success(request, "Comment updated successfully!")
        else:
            messages.error(request, "Error updating comment.")

    else:
        # Pre-fill form with existing comment data for editing
        comment_form = CommentForm(instance=comment)

    # Render the game detail page with updated context
    context = {
        "game": game,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "is_admin": request.user.is_superuser,
        "editing_comment_id": comment_id,  # Pass the ID of the comment being edited
    }
    return render(request, "gamelibrary/game_detail.html", context)

# View to delete comments

@login_required
def comment_delete(request, slug, comment_id):
    print("comment delete method called")
    """
    Delete a comment from a game post.

    This view allows a user to delete their own comment. It checks if the
    current user is the author of the comment before allowing deletion.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the game post.
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the game detail page after processing.

    Messages:
        SUCCESS: If the comment is successfully deleted.
        ERROR: If the user tries to delete a comment they don't own.
    """
    if request.method == "POST":
            queryset = Game.objects.all()
            post = get_object_or_404(queryset, slug=slug)
            comment = get_object_or_404(Comment, pk=comment_id)
            
            if comment.author == request.user or request.user.is_superuser:
                comment.delete()
                return JsonResponse({"success": True, "message": "Comment deleted successfully"})
            else:
                return JsonResponse({"success": False, "message": "You can only delete your own comments"})
        
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)


# View for search function


def search_view(request):
    """
    Search for games and comments based on a query string.

    This view handles search functionality across games and comments. It filters
    games by name, console, and date, and comments by body and author username.

    Args:
        request (HttpRequest): The HTTP request object containing the search query.

    Returns:
        HttpResponse: Renders the search results page with the context containing
                    the query, matching games, and matching comments.

    Context:
        query (str): The search query string.
        games (QuerySet): A queryset of Game objects matching the search criteria.
        comments (QuerySet): A queryset of Comment objects matching the search criteria.
    """
    query = request.GET.get("q", "")
    if query:
        games = Game.objects.filter(
            Q(name__icontains=query)
            | Q(console__icontains=query)
            | Q(date__icontains=query)
        )
        comments = Comment.objects.filter(
            Q(body__icontains=query) | Q(author__username__icontains=query)
        )
    else:
        games = Game.objects.none()
        comments = Comment.objects.none()

    context = {
        "query": query,
        "games": games,
        "comments": comments,
    }
    return render(request, "gamelibrary/search.html", context)

# Class-based views for superuser CRUD


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class GameCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = "gamelibrary/game_form.html"
    success_url = reverse_lazy("home")  # Redirect to homepage after creation

    def form_valid(self, form):
        messages.success(self.request, "Game created successfully.")
        return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = "gamelibrary/game_form.html"
    success_url = reverse_lazy("home")  # Redirect to homepage after update

    def form_valid(self, form):
        messages.success(self.request, "Game updated successfully.")
        return super().form_valid(form)


class GameDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy("home")  # Default redirect URL

    def form_valid(self, form):
        print("game delete method called")
        # Custom deletion logic here
        game_name = self.object.name  # Store game name for messaging
        
        # Call the superclass method to perform the actual deletion
        response = super().form_valid(form)

        # After deletion, set a success message
        messages.success(self.request, f"{game_name} has been deleted successfully.")
        return response  # Return the response from the superclass

    def get_success_url(self):
        return self.success_url  # Redirect to homepage after deletion

# IGDB API Views


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