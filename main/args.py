# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group # autorisation library
from django.contrib import auth # autorisation library


from login.models import User_data

from random import randint


# !!!!! IP GRABBER !!!!!
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# !!!!! Apkopots args !!!!!
def create_args(request):
    args = {}
   # USERNAME
    args['username'] = auth.get_user(request)
   # IP
    args['ip'] = get_client_ip(request)

   # MOBILE BROWSER OR TABLET
        # info: https://stackoverflow.com/questions/42273319/detect-mobile-devices-with-django-and-python-3
    args['mobile_browser'] = request.user_agent.is_mobile
    args['tablet_browser'] = request.user_agent.is_tablet

   # LOCATION
    try:
        args['location'] = User_data.objects.get(user_user = args['username']).map
    except:
        pass

   # BACKGROUN
    bg_int = randint(0, 1)
    if bg_int == 0:
        args['background'] = "images/back7.jpg"
    else:
        args['background'] = "images/back3.jpg"
   # FAVICON
    bg_int = randint(0, 3)
    if bg_int == 0:
        args['favicon'] = "images/favicon1.png"
    elif bg_int == 1:
        args['favicon'] = "images/favicon2.png"
    elif bg_int == 2:
        args['favicon'] = "images/favicon3.png"
    else:
        args['favicon'] = "images/favicon4.png"

   # DEVICE
    args['device'] = ""
    temp = request.user_agent.device
    if temp.family is not None:
        args['device'] += str(temp.family) + " "
    if temp.brand is not None:
        args['device'] += str(temp.brand) + " "
    if temp.model is not None:
        args['device'] += str(temp.model)
    args['device'] = args['device'].rstrip()


    return args
