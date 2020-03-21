# -*- coding: utf-8 -*-
from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

from smhouse.models import TermoAdress, TermoPlace, TermoReading

from login.models import User_data # Access data

from main.args import create_args

#import socket
#import json

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

# !!!!!!!!!!!!!!!!!!
# !!! Termo data !!!
# !!!!!!!!!!!!!!!!!!
    args['adress'] = TermoAdress.objects.all().order_by('order')


# ACCESS GRANTED
    response = render( request, 'termo.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/termo/', path='/' )
    return response
