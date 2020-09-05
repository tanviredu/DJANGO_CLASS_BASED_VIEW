from django import forms
from .models import GeekModel

class GeekForm(forms.ModelForm):
    class Meta:
        model  = GeekModel
        fields = ["title","description"] 