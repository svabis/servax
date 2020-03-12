# -*- coding: utf-8 -*-
from django.forms import ModelForm

from galery.models import Galery

from django import forms


class GaleryAddForm(ModelForm):
    class Meta:
        model = Galery
        fields = ('galery_date', 'galery_tags', 'galery_img', 'galery_public')

        galery_img = forms.ImageField()

#        widgets = {
#            'galery_tags': forms.TextInput( attrs={'class': 'form-control', 'size': 50 }),
#            'galery_date': forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
#            }
