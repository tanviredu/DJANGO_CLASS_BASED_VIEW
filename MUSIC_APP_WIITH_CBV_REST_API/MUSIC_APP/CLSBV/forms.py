from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):

    release_date = forms.DateField(widget = forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Album
        fields = "__all__"