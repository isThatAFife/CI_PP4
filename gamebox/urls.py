from django.contrib import admin
from django.urls import include, path
from gamelibrary import views

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("gamelibrary.urls"), name="gamelibrary-urls"),
    path("search/", views.search_view, name="search"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
]

handler403 = 'gamelibrary.views.permission_denied_view'
