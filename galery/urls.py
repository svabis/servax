# -*- coding: utf-8 -*-
from django.urls import path

# import views
from galery.views import *

urlpatterns = [
# GALERIJA PIEVIENOT
    path('add/', galery_add),

# IZVĒLE PĒC TAGA
    path('tag=<str:tag>/<int:pageid>/', galery_tags),
    path('tag=<str:tag>/', galery_tags),

# GALERIJA (with page number)
    path('<int:pageid>/', galery_main, name='galery_main'),

# GALERIJA (MAIN)
    path('', galery_main, name='galery_main'),

]
