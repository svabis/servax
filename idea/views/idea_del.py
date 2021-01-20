# -*- coding: utf-8 -*-
from django.shortcuts import redirect

from django.contrib.auth.models import User     # Django Users library
from django.contrib import auth # autorisation library

from main.args import create_args

from idea.models import Theme, Post

# ================================================================================
# POST DEL FOR USER ONLY
def del_post(request, p_id):
    try:
        p = Post.objects.get( id=p_id )
    except:
        return redirect ('/idea/')

    args = create_args(request)

    if p.user == args['username']:
       # get parent Theme
        t = Theme.objects.get(id = p.relate_to.id)
       # delete post
        p.delete()

       # update Theme entry count in cascade up to parent...parent e.t.c.
        while t.parent != None:
            t.entry_count -= 1
            t.save()
            t = t.parent

        if t.parent == None:
            t.entry_count -= 1
            t.save()

    if 'page_loc' in request.COOKIES:
        ret_loc = str(request.COOKIES.get('page_loc'))
    else:
        ret_loc = '/idea/'

    response = redirect( ret_loc )
    return response
