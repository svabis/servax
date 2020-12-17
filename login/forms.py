# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import MapPlot
from django import forms


# ======================================================================================
class MapPlotForm(ModelForm):

    class Meta:
        model = MapPlot
        fields = ['mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']

#'date', 'mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
