# -*- coding: utf-8 -*-
from django.urls import path

from login.views import login, logout

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
]
