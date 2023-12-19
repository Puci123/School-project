from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tag, Game, GameList, Review
from .forms import GameForm



# Create your views here.

def nothing(response):
    return HttpResponseRedirect(reverse("home"))


def home(response):
    return render(response, "main_app/home.html", {})


def add_game(response):
    exists = False
    if response.method == "POST":
        form = GameForm(response.POST, response.FILES)

        if form.is_valid():
            if not Game.objects.filter(title=form.cleaned_data["title"]):
                game = form.save()
                return HttpResponseRedirect(reverse("game site", args=(game.slug,)))
            else:
                exists = True
    else:
        form = GameForm()

    return render(response, "main_app/game_form.html", {"form": form, "exists": exists})


def game_site(response, g_slug):
    game = get_object_or_404(Game, slug=g_slug)
    return render(response, "main_app/game_site.html", {"game": game})



def search(response):
    search_str = response.GET.get("q")
    if search_str == None: search_str = ""

    games = Game.objects.filter(title__iregex=r'({})'.format(search_str))

    return render(response, "main_app/search.html", {"games": games, "search_str": search_str})