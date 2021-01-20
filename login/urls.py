# -*- coding: utf-8 -*-
from django.urls import path

from login.views import login, logout, change_password

urlpatterns = [
# LOGIN
    path('login/', login),
# LOGOUT
    path('logout/', logout),

# CHANGE PASSWORD
    path('password/', change_password, name='change_password'),
]
