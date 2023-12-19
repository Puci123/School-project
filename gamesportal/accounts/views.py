from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import GPUserCreationForm, GPUserChangeForm



# Create your views here.

class SignUpView(CreateView):
    form_class = GPUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def auth_logout(request):
    logout(request)
    return redirect('home')