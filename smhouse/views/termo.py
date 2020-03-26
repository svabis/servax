# -*- coding: utf-8 -*-
from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

from smhouse.models import TermoAdress, TermoPlace, TermoReading

from login.models import User_data # Access data

from main.args import create_args

# Import draw script
from smhouse.termo_draw import draw_termo_day

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
    adress = TermoAdress.objects.all().order_by('order')
    args['adress'] = adress

   # TermoAdress
    termo = TermoAdress.objects.all().order_by('order')

#    for t in termo
    args['ktc'] = TermoPlace.objects.filter( where = termo[0] )
    args['rpz'] = TermoPlace.objects.filter( where = termo[1] )

   # TermoPlaces
    args['ktc_day_ambient'] = TermoPlace.objects.filter(where = termo[0], ambient = True)
    args['ktc_day_data'] = TermoPlace.objects.filter(where = termo[0], ambient = False)

   # Date ranges
    args['termo_day']   = [datetime.now(), datetime.now() - timedelta(hours=24)]
    args['termo_week']  = [datetime.now(), datetime.now() - timedelta( days= 7)]
    args['termo_month'] = [datetime.now(), datetime.now() - timedelta( days=30)]

   # Draw Termo day layers
    draw_termo_day("ktc", True, "temp")
    draw_termo_day("ktc", False, "temp")

    response = render( request, 'termo.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/termo/', path='/' )
    return response
