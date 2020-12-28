# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.urls import path

from .views import plot, plot_edit, plot_del, plot_search


urlpatterns = [
# SEARCH
    path(r'search/', plot_search),

# DELETE
    path(r'plot/del/<int:d_id>/', plot_del),

# EDIT
    path(r'plot/<int:e_id>/', plot_edit, name="mapplot_edit"),

# MAIN & ADD NEW
    path(r'plot/', plot),

]
