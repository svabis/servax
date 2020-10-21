# -*- coding: utf-8 -*-
from django.http import HttpResponse # for button calls e.t.c
from django.shortcuts import render, redirect

from django.utils import timezone

from button.models import Meeting, MeetingPaticipant, MeetingButton

from button.forms import MeetingPaticipantForm

from main.args import create_args


# =================================================================================
def host(request):
    args = create_args(request)
    try:
        m = Meeting.objects.filter(creator = args["username"])
        c = m.count()
        m = m[c-1]
        args["meetings"] = m
        args["m"] = True
    except:
        pass

   # DATI
    args["mp"] = MeetingPaticipant.objects.filter( meeting = m).order_by("-date_added")
    args["mbp"] = MeetingButton.objects.filter( meeting = m ).order_by("-date_pushed")

   # ASK TO PUSH
    if request.POST:
        if m.push == True:
            m.push = False
        else:
            m.push = True
            args["pushed"] = True
        m.save()

    response = render( request, 'host.html', args )
    return response



# !!!!! Pievienot jaunu meetingu !!!!!
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
def push(request):
   # get data from request
    m_id = request.GET['data']
    p_id = int( request.GET['p_id'] )
    t = request.GET['time']

   # get Meeting & Participant
    try:
        m = Meeting.objects.get( url = m_id )
        p = MeetingPaticipant.objects.get( id = p_id )
    except:
        response = HttpResponse('error')
        return response

    temp = MeetingButton( participant = p, meeting = m, time_remaining = t )
    temp.save()

    response = HttpResponse("ok")
    return response

# =================================================================================
def press(request):
   # get data from request
    m_id = request.GET['data']
    p_id = request.GET['p_id']

   # get Meeting
    try:
        m = Meeting.objects.get( url = m_id )
    except:
        response = HttpResponse('error')
        return response

   # Get Participant
    try:
        p = MeetingPaticipant.objects.get( id = int(p_id) )
    except:
        response = HttpResponse('error')
        return response

   # IF Meeting ended
    if m.end == True:
        response = HttpResponse('ended')
        return response

   # Activate participiant
    p.date_active = timezone.now()
    p.active = True
    p.save()

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
