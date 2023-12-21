from django.urls import path
from . import views



# Add url paths here.

urlpatterns = [
    path("", views.nothing, name="nothing"),
    path("home/", views.home, name="home"),
    path("addgame/", views.add_game, name="add game"),
    path("game/<slug:g_slug>/", views.game_site, name="game site"),
    path("search/", views.search, name="search"),
]