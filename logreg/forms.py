
from django import forms 
from .models import *
  
class ArtistImageForm(forms.ModelForm): 
    class Meta: 
        model = ArtistImage 
        fields = ['artist_image']

class ArtistLinkForm(forms.Form):
    link = forms.URLField()

