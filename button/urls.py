# -*- coding: utf-8 -*-
from django.urls import path

from button.views import *

urlpatterns = [
   # HOST ENTRANCE
    path('host/', host),
   # HOST ADD MEETING
    path('host/add/', add_meeting),

# ===========================================================
    path('press/', press),

   # join login
   # join POST --> redirect (participqte)
    path('join/<str:m_id>/', join),

# MAIN --> PARTICIPANT EENTRY
    path('', participate, name='participate'),
]
