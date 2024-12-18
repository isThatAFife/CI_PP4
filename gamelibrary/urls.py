from . import views
from django.urls import path
from .views import GameDeleteView

urlpatterns = [
    path("", views.GameList.as_view(), name="home"),
    path("my-comments/", views.user_comments, name="user_comments"),
    path("search/", views.search_view, name="search"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
    path(
        "game/<slug:slug>/comment/<int:comment_id>/edit/",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "game/<slug:slug>/comment/<int:comment_id>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("game/new/", views.GameCreateView.as_view(), name="game_create"),
    path(
        "game/<slug:slug>/edit/",
        views.GameUpdateView.as_view(),
        name="game_update",
    ),
    path(
        "game/<slug:slug>/delete/",
        GameDeleteView.as_view(),
        name="game_delete",
    ),
]
