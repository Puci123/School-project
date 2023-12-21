from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tag, Game, GameList, Review
from .forms import GameForm, ReviewForm



# Create your views here.

def nothing(request):
    return HttpResponseRedirect(reverse("home"))


def home(request):
    return render(request, "main_app/home.html", {})


def add_game(response):
    if response.user.is_superuser:
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
    else:
        HttpResponseRedirect(reverse("home"))


def game_site(request, g_slug):
    game = get_object_or_404(Game, slug=g_slug)
    return render(request, "main_app/game_site.html", {"game": game})


def review_site(request, g_slug):
    game = get_object_or_404(Game, slug=g_slug)
    reviews = Review.objects.filter(game=game)

    if request.user.is_authenticated:
        curr_rev = reviews.filter(user=request.user)
        if curr_rev: curr_rev = curr_rev[0]
    else:
        curr_rev = None

    return render(request, "main_app/reviews.html", {"game": game, "reviews": reviews, "curr_rev": curr_rev})


def write_review(response, g_slug):
    if response.user.is_authenticated:
        game=Game.objects.filter(slug=g_slug)
        rev = Review.objects.filter(user=response.user)
        if game and not rev.filter(game=game[0]):
            if response.method == "POST":
                form = ReviewForm(response.POST)

                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = response.user
                    review.game = game[0]
                    review.likes = 0
                    review.dislikes = 0
                    review.save()

                    return HttpResponseRedirect(reverse("review site", args=(g_slug,)))
            else:
                form = ReviewForm()

            return render(response, "main_app/write_review.html", {"form": form})
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("login"))


def search(response):
    search_str = response.GET.get("q")
    if search_str:
        games = Game.objects.filter(title__icontains=search_str)
    else:
        search_str = ""
        games = Game.objects.all()

    return render(response, "main_app/search.html", {"games": games, "search_str": search_str})