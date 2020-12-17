# -*- coding: utf-8 -*-
from django.forms import ModelForm
from jobs.models import Jobs, JobObj
from django import forms


TYPE_CHOICES = (
    ('maja', 'māja'),
    ('IT', 'IT'),
    ('lapene', 'lapene'),
    ('skjunis', 'šķūnis'),
    ('elektriba', 'elektrība'),
    ('santehnika', 'santehnika'),
    ('instrument', 'instrumenti'),
    ('darzs', 'dārzs'),
    ('zogs', 'žogs'),
    ('grods', 'grods'),
    ('koki', 'koki'),
    ('cits', 'cits'),
#    ('KUVALDA', 'TrailCamPhoto'),
#    ('GRAVANI', 'IT-Projekti'),
)

# ======================================================================================
class JobsForm(ModelForm):

    class Meta:
        model = Jobs
        fields = ['jobs_descr', 'jobs_zone', 'jobs_type', 'marked']

        widgets = {
            'jobs_descr': forms.Textarea(attrs={'class': 'form-control', 'rows' : '5'}),
            'jobs_zone': forms.Select(attrs={'class': 'form-control'}),
            'jobs_type': forms.Select(attrs={'class': 'form-control'}),
            'marked': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', True)
        super(JobsForm, self).__init__(*args, **kwargs)
        if not self.user:
            self.fields['jobs_zone'].choices = TYPE_CHOICES


# ======================================================================================
class JobsObjForm(ModelForm):
    class Meta:
        model = JobObj
        fields = ('obj_title', 'obj_descr', 'obj_zone', 'obj_actual')

        widgets = {
            'obj_title': forms.TextInput( attrs={'class': 'form-control', 'size': 50}),
            'obj_descr': forms.Textarea(attrs={'class': 'form-control', 'rows' : '3', 'autofocus' : 'autofocus'}),
            'obj_zone': forms.Select(attrs={'class': 'form-control'}),
            'obj_actual': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
