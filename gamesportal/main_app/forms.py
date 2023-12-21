from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from . import models



# Create your forms here.

class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ["title", "description", "release_date", "cover_image", "tags"]
    
    tags = forms.ModelMultipleChoiceField(queryset=models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()



class GameListForm(forms.ModelForm):
    class Meta:
        model = models.GameList
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()