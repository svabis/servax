# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.urls import path

# --------------
# import project settings for STATIC & MEDIA root ACCESS
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
# not needed if static & media is served in production using Alias
from django.conf.urls import url
# --------------

# -- ??? --
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# -- ??? --

# import views
from main.views import home, weather, location, denied, stats
from main.views import ai, r_web
from main.views import led_test
#from login.views import login, logout

from mapplot.views import plot

# import django admin, access admin only loged in users
from django.contrib.auth.decorators import login_required # LOGIN
from django.contrib import admin

admin.autodiscover()
admin.site.login = login_required(admin.site.login)


urlpatterns = [
# STATIC AND MEDIA
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),

# ADMIN
    path('adminlucy/', admin.site.urls),

# LOGIN
    path('login/', include('login.urls')),

# ACCESS DENIIED
    path('access_denied/', denied, name='access_denied'),

# MAP PLOTTER
    path('mapplot/', include('mapplot.urls')),

# AI TESTI
    path('ai/', ai),
# SIMPLE VIDEO WEB_SERVER
    path('r_web/', r_web),

# LED TESTS
    path('led_test/', led_test),

# JOBS
    path('jobs/', include('jobs.urls')),

# VIDEO
    path('video/', include('video.urls')),

# LOCATION & WEATHER
    path('weather/', weather),
    path('location/', location),

# STATISTICS
    path('stats/', stats),

# IDEA (previously GARDEN)
    path('idea/', include('idea.urls')),

# GALERY
    path('gallery/', include('galery.urls')),

# SMART HOUSE
    path('sm_house/', include('smhouse.urls')),

# MAIN
    path('', home),
]

# This doesn't work
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
