# -*- coding: utf-8 -*-
from django.urls import path

from button.views import *

urlpatterns = [
   # HOST ENTRANCE
   # HOST POST to push button for last Meeting
    path('host/', host),

   # HOST ADD MEETING
    path('host/add/', add_meeting),

# ===========================================================
   # test if need to be press & update Participant data
    path('press/', press),

   # push button
    path('push/', push),

   # join login
   # join POST --> redirect (participqte)
    path('join/<str:m_id>/', join),

# MAIN --> PARTICIPANT EENTRY
    path('', participate, name='participate'),
]
