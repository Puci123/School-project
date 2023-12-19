from django.urls import path
from . import views



# Add url paths here.

urlpatterns = [
    path("", views.home, name="home"),
    path("game/addgame", views.add_game, name="add game"),
    path("game/<slug:g_slug>", views.game_site, name="game site"),
    path("search", views.search, name="search"),
]