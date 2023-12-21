from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from . import models



# Create your forms here.

class GPUserCreationForm(UserCreationForm):
    class Meta:
        model = models.GPUser
        fields = ("username", "email", "password1", "password2", "decryption", "profile_picture")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class GPUserChangeForm(UserChangeForm):
    class Meta:
        model = models.GPUser
        fields = ("username", "email", "decryption","profile_picture")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()