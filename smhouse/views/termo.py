# -*- coding: utf-8 -*-
#from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

from login.models import User_data # Access data

from main.args import create_args

from smhouse.models import Location, TermoPlace, TermoReading

# Import draw script
from smhouse.termo_draw import draw_termo

from datetime import datetime, timedelta


# !!!!! TERMO VIEW !!!!!
def smhouse_termo(request, slug=""):
    args = create_args(request)
    args['heading'] = "Temperatūras"
    args['title'] = 'Gudrā Māja | Svabwilla'

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        termo_access = User_data.objects.get(user_user = args['username']).sm_termo
    if termo_access != True:
        return redirect('access_denied')

# ACCESS GRANTED

   # Date ranges
    args['termo_day']   = [datetime.now(), datetime.now() - timedelta(hours=24)]
    args['termo_week']  = [datetime.now(), datetime.now() - timedelta( days= 7)]
    args['termo_month'] = [datetime.now(), datetime.now() - timedelta( days=30)]

   # Get Termo Adress for tabs
    adress = Location.objects.all().order_by('order')
    args['adress'] = adress

   # set variable slug
    if slug == "":
        slug = adress[0].slug

    a = Location.objects.get( slug = slug )
    args['slug'] = slug

    out_data = []

    if True:
#    for a in adress:
        args['data'] = TermoPlace.objects.filter( where = a ).order_by('order')

       # TermoPlaces
        args['data_ambient'] = TermoPlace.objects.filter( where = a, ambient = True )
        args['data_data'] = TermoPlace.objects.filter( where = a, ambient = False )
        args['data_humy'] = TermoPlace.objects.filter( where = a )

       # Draw Termo day
        draw_termo(a.slug, 24, 24, "%H", 1, "day", True)
        draw_termo(a.slug, 24, 24, "%H", 1, "day", False)
        draw_termo(a.slug, 24, 24, "%H", 1, "day", None)

#        if False in data:
#            data = False
#        else:
#            data = True

       # output is shown or not
#        out_data.append(data)

#    temp = []
#    for i, a in enumerate(adress):
#         temp.append( [a, out_data[i]] )
#    args['adress'] = temp


    response = render( request, 'termo.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/termo/', path='/' )
#    response.set_cookie( key='show_termo_graph', value='true', path='/', max_age=20 )
    return response
