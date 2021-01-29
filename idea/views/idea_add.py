# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.contrib.auth.models import User     # Django Users library
from django.contrib import auth # autorisation library

from login.models import User_data # Access data
from main.args import create_args

from idea.models import SuperTheme, Theme, Post
from idea.forms import PostForm, ThemeForm

import unicodedata
import slugify
import math
import random
import string


# Add theme
def add_tema(request):
    args = create_args(request)
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        idea_access = User_data.objects.get(user_user = args['username']).idea
    if idea_access != True:
      # ACCESS DENIED
        return redirect('access_denied')

    try:
        idea_add = User_data.objects.get(user_user = args['username']).idea_add
    except:
        idea_add = False

    args['super'] = SuperTheme.objects.all().order_by('order')
    args['user'] = auth.get_user(request)

    if request.POST and idea_add:
        form = ThemeForm( request.POST )

        location = str(request.COOKIES.get('page_loc')).split('/')

        if form.is_valid():
           # RETRIEVE ALL SLUG
            st = list(SuperTheme.objects.values_list('slug', flat=True))
            ts = list(Theme.objects.values_list('slug', flat=True))
            slugs = st + ts

            new_tema = form.save( commit=False )
            new_tema.relate_to_super = SuperTheme.objects.get( slug = location[2] )

            new_tema.created_by = auth.get_user(request)
#            new_tema.save()

           # Create Tema slug from title
            slug = form.cleaned_data.get('title').replace("/", "")
            slug = unicodedata.normalize('NFKD', slug).encode('ascii','ignore')

            while slug in slugs:
                slug = slug + random.choice(string.ascii_letters)
            new_tema.slug = slug

            try:
                if len(location[3]) != 0:
                    new_tema.parent = Theme.objects.get( slug = location[3] )
            except:
                new_tema.parent = None

            new_tema.save()

       # REDIRECT TO PAGE OF ORIGIN
        if str('page_loc') in request.COOKIES:
            response = redirect( str(request.COOKIES.get('page_loc')) )
        else:
            response = redirect( '/idea/' )
        return response

    return redirect('/idea/')
