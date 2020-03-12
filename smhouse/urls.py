# -*- coding: utf-8 -*-
from django.urls import path

# import views
from smhouse.views import *


urlpatterns = [
# ELEKTRO DATA UPLOAD
    path('electro/input_data/', smhouse_electro_input_data),
# ELEKTRO DATA VIEWS
    path('electro/', smhouse_electro_main, name='electro_main'),

# ELEKTRO DATA VIEWS
    path('led_control/', led_control),
    path('led/', smhouse_led, name='sm_led'),

# TERMO
    path('termo/', smhouse_termo),
]
