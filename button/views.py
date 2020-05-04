# -*- coding: utf-8 -*-
from django.http import HttpResponse # for button calls e.t.c
from django.shortcuts import render, redirect

from button.models import Meeting, MeetingPaticipant, MeetingButton

from button.forms import MeetingPaticipantForm

from main.args import create_args


# =================================================================================
def host(request):
    args = create_args(request)

    args["meetings"] = Meeting.objects.filter(creator = args["username"])
    response = render( request, 'host.html', args )
#    response.set_cookie( key='page_loc', value='/video/archive/', path='/' )
    return response


def add_meeting(request):
    if request.POST:
        form = KlientsForm( request.POST )
        if form.is_valid():
           # SLUGIFY "Vārds Uzvārds" --> "vards_uzvards"
            new_name = slugify(form.cleaned_data['vards']).lower()
            new_email = form.cleaned_data['e_pasts'].lower()
            new_tel = form.cleaned_data['tel']

    return redirect("/button/host/")

# =================================================================================
def press(request):
    m_id = request.GET['data']
    try:
        m = Meeting.objects.get( url = m_id )
    except:
        response = HttpResponse('error')
        return response

    if m.end == True:
        response = HttpResponse('ended')
        return response

    resp = ""
    if m.push == True:
        resp = "push "
        if m.timer == None:
            resp = resp + "60"
        else:
            resp = resp + str(m.timer)

    response = HttpResponse( resp )
    return response


# =================================================================================
# !!!!! pievienoties mītingam !!!!!
def join(request, m_id=""):
    args = create_args(request)
    try:
        m = Meeting.objects.get( url = m_id )
       # meetings ir beidzies
        if m.end == True:
            args["ended"] = True
            response = render( request, 'join.html', args )
            return response
        args["meeting"] = m
    except:
       # Nav tāda meetinga
        args["m_error"] = True
        response = render( request, 'join.html', args )
        return response

    args["form"] = MeetingPaticipantForm
    args["m_id"] = m.url
   # add new participant
    if request.POST:
        form = MeetingPaticipantForm( request.POST )

        if form.is_valid():
            temp = form.save( commit = False )
            temp.meeting = m
            temp.active = True
            temp.save()

            c = m.url + ":" + str( temp.id )

            response = redirect( 'participate' )
            response.set_cookie( key='button', value=c, path='/' )
            return response

    response = render( request, 'join.html', args )
    return response

# !!!!! mītings + buttons !!!!!
def participate(request):
    args = create_args(request)
#    try:
    if True:
        c = request.COOKIES.get('button').split(":")
        m = Meeting.objects.get( url = c[0] )
        args["title"] = m.title

        u = MeetingPaticipant.objects.get( id = int(c[1]) )
        args["m_user"] = u
#    except:
#        pass

    response = render( request, 'participant.html', args )
    return response
