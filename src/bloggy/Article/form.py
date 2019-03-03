from django import forms
from .models import article


class article_form(forms.ModelForm):
    class Meta:
        model = article
        fields=[
           'title',
        ]