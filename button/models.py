# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Django useri
from django.contrib.auth.models import User

#import datetime

import uuid

def meeting_id():
    return "test"

# !!!!! Meetings ko veido useris (hosts) !!!!!
class Meeting(models.Model):
    class Meta():
        db_table = "button_meeting"

   # autors
    creator = models.ForeignKey( User, blank=True, null=True, on_delete=models.CASCADE )
   # izveidots
    date_added = models.DateTimeField( default=timezone.now )
   # notikuma nosaukums
    title = models.CharField(max_length = 200, blank=True, null=True)
   # dalības url
    url = models.SlugField( unique=True, default=str(uuid.uuid4()).split('-')[-1] )
   # beidzās
    end = models.BooleanField( default=False )
   # spied
    push = models.BooleanField( default=False )
   # timer
    timer = models.IntegerField( null=True, blank=True )

class MeetingPaticipant(models.Model):
    class Meta():
        db_table = "button_participant"

   # kurš meetings
    meeting = models.ForeignKey( Meeting, blank=True, null=True, on_delete=models.CASCADE )
   # vārds vai ID
    participiant = models.CharField(max_length = 100, blank=True, null=True)
   # izveidots
    date_added = models.DateTimeField( default=timezone.now )
   # aktīvs
    date_active = models.DateTimeField( default=timezone.now )
    active = models.BooleanField( default=False )

    def __str__(self):
        return str(self.participiant)

class MeetingButton(models.Model):
    class Meta():
        db_table = "button_button"

   # kurš spiež
    participant = models.ForeignKey( MeetingPaticipant, blank=True, null=True, on_delete=models.CASCADE )
   # kurš meetings
    meeting = models.ForeignKey( Meeting, blank=True, null=True, on_delete=models.CASCADE )
   # nospiests
    date_pushed = models.DateTimeField( default=timezone.now )
   # atlicis laiks
    time_remaining = models.CharField(max_length = 10, blank=True, null=True)
