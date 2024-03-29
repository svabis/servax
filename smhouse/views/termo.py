# -*- coding: utf-8 -*-
from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

from login.models import User_data # Access data

from main.args import create_args

from smhouse.models import Location, TermoPlace, TermoReading

# Import draw script
from smhouse.termo_draw import draw_termo

from datetime import datetime, timedelta, date


# !!!!! TERMO VIEW !!!!!
def smhouse_termo(request, slug=""):
    args = create_args(request)
    args['heading'] = "Temperatūras"
    args['title'] = 'Gudrā Māja | Svabwilla'

   # enable zoom on mobile device
    args["mobile_zoom"] = True

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        termo_access = User_data.objects.get(user_user = args['username']).sm_termo
    if termo_access != True:
        return redirect('access_denied')

# ACCESS GRANTED

   # Date ranges
    args['termo_day']   = [datetime.now() - timedelta(hours=24), datetime.now()]
    args['termo_week']  = [datetime.now() - timedelta( days= 7), datetime.now()]
    args['termo_month'] = [datetime.now() - timedelta( days=30), datetime.now()]
    args['termo_year']  = [datetime.now() - timedelta(days=365), datetime.now()]

    if datetime.now().hour > 12:
        args['hours'] = "12:00"
    else:
        args['hours'] = "00:00"

   # Get Termo Adress for tabs
    adress = Location.objects.all().order_by('order')
    args['adress'] = adress

   # set variable slug
    if slug == "":
        if User_data.objects.get(user_user = args['username']).location is not None:
            slug = User_data.objects.get(user_user = args['username']).location.slug
        else:
            slug = adress[0].slug

    a = Location.objects.get( slug = slug )
    args['slug'] = slug

    args['data'] = TermoPlace.objects.filter( where = a ).order_by('order')

   # TermoPlaces
    args['data_ambient'] = TermoPlace.objects.filter( where = a, ambient = True )
    args['data_data'] = TermoPlace.objects.filter( where = a, ambient = False )
    args['data_humy'] = TermoPlace.objects.filter( where = a )

   # Draw Termo day
    import threading
    d1 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", True ), daemon=True)
    d1.start()
    d2 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", False ), daemon=True)
    d2.start()
    d3 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", None ), daemon=True)
    d3.start()

   # rand for image cache reload
    import random
    args['cache'] = "?=" + str(random.randint(20,99))

    response = render( request, 'termo.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/termo/', path='/' )
#    response.set_cookie( key='show_termo_graph', value='true', path='/', max_age=20 )
    return response


# ==========================================================================================
def smhouse_termo_update(request, slug=""):
    args = create_args(request)
# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return HttpResponse('fail')
    else:
        termo_access = User_data.objects.get(user_user = args['username']).sm_termo
    if termo_access != True:
        return HttpResponse('fail')

# ACCESS GRANTED
    a = Location.objects.get( slug = slug )

   # Draw Termo day
    import threading
    d1 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", True ), daemon=True)
    d1.start()
    d2 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", False ), daemon=True)
    d2.start()
    d3 = threading.Thread(target=draw_termo, args=( a.slug, 24, 24, "%H", 1, "day", None ), daemon=True)
    d3.start()

    return HttpResponse('done')

