# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import Post, Theme

# Ieraksts
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'url')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows' : '5', 'style':'resize:none;'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'image': forms.FileInput(),
        }

# Tema/Diskusija
class ThemeForm(ModelForm):
    title = forms.CharField( max_length=100, required=True, label='Tēmas/Diskusijas nosaukums', help_text='Obligāti jāaizpilda',
        widget = forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}) )

    class Meta:
        model = Theme
        fields = ('title', 'comment')
