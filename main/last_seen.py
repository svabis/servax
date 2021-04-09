#from django.contrib.sites.models import Site
from login.models import User_data
from django.utils.timezone import now
import datetime
import pytz


class SetLastVisitMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
     # !!!!! INSERT CODE HERE !!!!!
   # CHECK IF user_last_visit is older than ??? (10 min)
#        if False:
#        if request.user.is_authenticated():
        if request.user.is_authenticated:
           # User_data object list
            user = User_data.objects.filter(user_user = request.user.pk)

            for usr in user:
                user_visit = getattr(usr, 'user_last_visit')
                time_now = datetime.datetime.now().replace(tzinfo=pytz.timezone('EET'))

               #10 MINUTES
                timeDiff = ( time_now - user_visit ).total_seconds()
                if timeDiff > 600:
                # Update last visit time after request finished processing.
#                   User_data.objects.filter(user_user=request.user.pk).update( user_last_visit = now() )
                    usr.user_last_visit = now()
                    usr.save()

        response = self.get_response(request)
        return response



#from django.contrib.auth.backends import BaseBackend

# !!!!! EMPTY MIDDLEWARE TEMPLATE !!!!!
# !!!!!         NOT IN USE        !!!!!
class TestMiddleware: #(BaseBackend):

  def __init__(self, get_response):
      self.get_response = get_response

  def __call__(self, request):
     # !!!!! INSERT CODE HERE !!!!!

      response = self.get_response(request)
      return response
