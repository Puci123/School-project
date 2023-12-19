from django import forms
from . import models



# Create your forms here.

class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ["title", "description", "release_date", "cover_image", "tags"]
    
    tags = forms.ModelMultipleChoiceField(queryset=models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple)