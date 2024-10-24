from django import forms
from . import models
class homeform(forms.ModelForm):
    class Meta:
        model=models.store
        fields="__all__"
        labels={
            "fname": "enter your name",
            "fpass" : "enter your pass",
        }