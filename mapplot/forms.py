# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import MapPlot
from django import forms


# ======================================================================================
class MapPlotForm(ModelForm):

    class Meta:
        model = MapPlot
        fields = ['mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']

        widgets = {
            'mark': forms.TextInput(attrs={'class': 'form-control'}),

            'city': forms.Select(attrs={'class': 'form-control'}),

            'lat': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly'}),
            'lon': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly'}),

            'radio': forms.Select(attrs={'class': 'form-control'}),
            'chk_1': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
            'chk_2': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
            'chk_3': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
        }

#'date', 'mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
