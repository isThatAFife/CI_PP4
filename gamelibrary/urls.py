from . import views
from django.urls import path

urlpatterns = [
    path("", views.GameList.as_view(), name="home"),
    path("my-comments/", views.user_comments, name="user_comments"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    path("search/", views.search_view, name="search"),
    path('game/new/', views.GameCreateView.as_view(), name='game_create'),
    path('game/<slug:slug>/edit/',
         views.GameUpdateView.as_view(), name='game_update'),
    path('game/<slug:slug>/delete/',
         views.GameDeleteView.as_view(), name='game_delete'),
]
