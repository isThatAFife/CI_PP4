from . import views
from django.urls import path

urlpatterns = [
    path("", views.GameList.as_view(), name="home"),
    path("my-comments/", views.user_comments, name="user_comments"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
]
