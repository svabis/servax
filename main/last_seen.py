#from django.contrib.sites.models import Site
from login.models import User_data
from django.utils.timezone import now
import datetime
import pytz


class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            # CHECK IF user_last_visit is older than ??? (10 min)
            user = User_data.objects.filter(user_user = request.user.pk)		# User_data object list

            for usr in user:
                user_visit = getattr(usr, 'user_last_visit')
                time_now = datetime.datetime.now().replace(tzinfo=pytz.timezone('EET'))

                timeDiff = ( time_now - user_visit ).total_seconds()
                if timeDiff > 600:	#10 MINUTES
                # Update last visit time after request finished processing.
#                   User_data.objects.filter(user_user=request.user.pk).update( user_last_visit = now() )
                    usr.user_last_visit = now()
                    usr.save()

        return response
