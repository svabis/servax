# -*- coding: utf-8 -*-
from login.models import User_data

from django.utils.timezone import now

import datetime
import pytz


# ========================================================================================
class SetLastVisitMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

           # User_data object filter by primary key
            user = User_data.objects.filter(user_user = request.user.pk)

            for u in user:
                user_visit = getattr(u, 'user_last_visit')

               # CHECK IF user_last_visit is older than ??? (10 min)
                time_now = datetime.datetime.now().replace(tzinfo=pytz.timezone('EET'))
                timeDiff = ( time_now - user_visit ).total_seconds()

                if timeDiff > 600:
                   # Update last visit time while request is being processed
                    u.user_last_visit = now()
                    u.save()

        response = self.get_response(request)
        return response


# ========================================================================================
def redrawTermoDay():
    from smhouse.models import Location
    from smhouse.termo_draw import draw_termo

    from time import sleep

    for _ in range(0,10):
        sleep(60)
        for a in Location.objects.all():
            draw_termo( a.slug, 24, 24, "%H", 1, "day", True )
            draw_termo( a.slug, 24, 24, "%H", 1, "day", False )
            draw_termo( a.slug, 24, 24, "%H", 1, "day", None )


class TermoUpdateMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            if '/sm_house/termo/' in request.path:
                import threading
                t = threading.Thread(target=redrawTermoDay, args=(), daemon=True)
                t.start()



        response = self.get_response(request)
        return response




# ========================================================================================
# !!!!! EMPTY MIDDLEWARE TEMPLATE !!!!!
# !!!!!         NOT IN USE        !!!!!

#from django.contrib.auth.backends import BaseBackend

class TestMiddleware: #(BaseBackend):

  def __init__(self, get_response):
      self.get_response = get_response

  def __call__(self, request):
     # !!!!! INSERT CODE HERE !!!!!

      response = self.get_response(request)
      return response
