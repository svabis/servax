# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import auth

from login.models import User_data

from main.args import create_args


# !!!!! LOG-IN !!!!!
def login(request):
    args = create_args(request) # create new argument list
#    args.update(csrf(request))      # encript data
    args['heading'] = "Autorizēšanās"

    if request.POST: # actions if login Form is submitted
        username = request.POST.get('username', '') # usermname <= get variable from Form (name="username"), if not leave blank
        password = request.POST.get('password', '') # password <= get variable from Form (name="password"), if not leave blank
        user = auth.authenticate( username = username, password = password ) # new variable --> user from auth system

        if user is not None: # auth return None if this user does not exit, if not then:
            if user.is_active == False: # User is disabled in Django Admin -->
                args['login_error'] = "Lietotājs uz doto momentu ir bloķēts"
                return render( request, 'login.html', args )

            auth.login( request, user ) # authorizate user from Form
            if 'page_loc' in request.COOKIES:
                ret_loc = str(request.COOKIES.get('page_loc'))
            else:
                ret_loc = '/'
            rd = redirect( ret_loc )
            rd.set_cookie('ret', 'True', max_age=10) # 10 second Cookie for not changing sort order
            return rd

        else: # if user does not exist:
            args['login_error'] = "Lietotājs nav atrasts"
            return render( request, 'login.html', args )

    else: # actions if activated hyperlink to login Form
        return render( request, 'login.html', args )


# !!!!! LOG-OUT !!!!!
def logout(request):
    auth.logout(request)
    username = None
    return redirect('/')


# !!!!! CHANGE PASSWORD !!!!!
def change_password(request):
    args = create_args(request)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    args['form'] = form
    return render( request, 'change_password.html', args )
