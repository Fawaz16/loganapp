import imp
from typing import Text
from django import forms


class ContactForm(forms.Form):
    Name= forms.CharField(max_length=200)
    Package= forms.CharField(max_length=200)
    Email=forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea(attrs={'class':'custom-textarea', 'rows':5}))
    Number=forms.CharField(max_length=200)