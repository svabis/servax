# -*- coding: utf-8 -*-
from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

from smhouse.models import Location, TermoPlace, TermoReading

from login.models import User_data # Access data

from main.args import create_args

# Import draw script
#from smhouse.termo_draw import draw_termo_day
from smhouse.termo_draw import draw_termo

from datetime import datetime, timedelta


# !!!!! LED VIEW !!!!!
def smhouse_termo(request):
    args = create_args(request)
    args['heading'] = "Temperatūras"
    args['title'] = 'Gudrā Māja | Svabwilla'

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        elektr_access = User_data.objects.get(user_user = args['username']).sm_termo
    if elektr_access != True:
        return redirect('access_denied')

# ACCESS GRANTED

   # Termo Adress
    adress = Location.objects.all().order_by('order')
    args['adress'] = adress

    termo = adress

#    for t in termo
    args['ktc'] = TermoPlace.objects.filter( where = termo[0] )
    args['rpz'] = TermoPlace.objects.filter( where = termo[1] )

   # TermoPlaces
    args['ktc_ambient'] = TermoPlace.objects.filter( where = termo[0], ambient = True )
    args['ktc_data'] = TermoPlace.objects.filter( where = termo[0], ambient = False )
    args['ktc_humy'] = TermoPlace.objects.filter( where = termo[0] )

   # Date ranges
    args['termo_day']   = [datetime.now(), datetime.now() - timedelta(hours=24)]
    args['termo_week']  = [datetime.now(), datetime.now() - timedelta( days= 7)]
    args['termo_month'] = [datetime.now(), datetime.now() - timedelta( days=30)]
    args['termo_year']  = [datetime.now(), datetime.now() - timedelta(days=365)]

   # Draw Termo day
    draw_termo("ktc", 24, 24, "%H", 1, "day", True)
    draw_termo("ktc", 24, 24, "%H", 1, "day", False)
    draw_termo("ktc", 24, 24, "%H", 1, "day", None)

    response = render( request, 'termo.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/termo/', path='/' )
    return response
