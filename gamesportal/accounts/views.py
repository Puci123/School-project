from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import GPUserCreationForm, GPUserChangeForm, UserProfileForm, PasswordChangeForm
from main_app.models import GameList, Game
from main_app.forms import GameListForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUpView(CreateView):
    form_class = GPUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def auth_logout(request):
    logout(request)
    return redirect('home')


def account_site(request):
    if request.user.is_authenticated:
        return render(request, "accounts/account_site.html", {})
    else:
        return HttpResponseRedirect(reverse("login"))


def game_lists_site(response):
    if response.user.is_authenticated:
        game_lists = GameList.objects.filter(user=response.user)

        if game_lists and response.method == "POST":
            list_id = response.POST.get("del_list")
            if list_id:
                list = GameList.objects.get(id=list_id)
                list.delete()
                
                game_lists = GameList.objects.filter(user=response.user)

        return render(response, "accounts/game_lists_site.html", {"game_lists": game_lists})
    else:
        return HttpResponseRedirect(reverse("login"))


def game_list(response, gl_slug):
    if response.user.is_authenticated:
        list = GameList.objects.get(user=response.user, slug=gl_slug)

        if list and response.method == "POST":
            game_id = response.POST.get("add_game")
            if game_id:
                game = Game.objects.get(id=game_id)
                list.games.add(game)
            
            game_id = response.POST.get("del_game")
            if game_id:
                game = Game.objects.get(id=game_id)
                list.games.remove(game)

        id_list = list.games.values_list("id", flat=True)

        return render(response, "accounts/game_list.html", { "list": list, "all_games": Game.objects.exclude(id__in=id_list) })
    else:
        return HttpResponseRedirect(reverse("login"))


def list_form(response):
    if response.user.is_authenticated:
        exists = False
        if response.method == "POST":
            form = GameListForm(response.POST)

            if form.is_valid():
                if not GameList.objects.filter(title=form.cleaned_data["title"], user=response.user):
                    list = form.save(commit=False)
                    list.user = response.user
                    list.save()
                    return HttpResponseRedirect(reverse("game list", args=(list.slug,)))
                else:
                    exists = True
        else:
            form = GameListForm()
            
        return render(response, "accounts/list_form.html", {"form": form, "exists": exists})
    else:
        return HttpResponseRedirect(reverse("login"))
    

def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm (request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account site')  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/account_edit.html', {'form': form})

@login_required
def change_password(request):
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)     # Keep the user logged in
            return redirect('account site')                  # Redirect to the user's profile page

    return render(request, 'accounts/change_password.html', {'password_form': password_form})

