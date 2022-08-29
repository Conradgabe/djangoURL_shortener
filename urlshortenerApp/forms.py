from django import forms

from .models import LinkURL

class LinkURLForm(forms.ModelForm):

    class Meta:
        model = LinkURL
        fields = ['original_url']