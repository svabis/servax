# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
#from django.core.files import File

from login.models import User_data

from datetime import datetime, date
#from time import sleep


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User_data.objects.all()

        for u in users:
#            print( "" )
#            print( u )
            if u.user_user.is_authenticated:
              print( u.user_user.username[0:6], "\t", u.user_user.is_authenticated )
            else:
              print( u.user_user )
#            print( u.user_user.get_session_auth_hash )
