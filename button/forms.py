# -*- coding: utf-8 -*-
from django.forms import ModelForm
from button.models import MeetingPaticipant
from django import forms


# ======================================================================================
class MeetingPaticipantForm(ModelForm):
    class Meta:
        model = MeetingPaticipant
        fields = [ 'participiant', 'active' ]
#        fields = ('meeting', 'participiant', 'date_added', 'date_active', 'active')


