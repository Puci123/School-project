from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import GPUserCreationForm, GPUserChangeForm
from .models import GPUser



# Register your models here.

class GPUserAdmin(UserAdmin):
    add_form = GPUserCreationForm
    form = GPUserChangeForm
    model = GPUser
    list_display = ["email", "username",]



admin.site.register(GPUser, GPUserAdmin)