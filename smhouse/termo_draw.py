# -*- coding: utf-8 -*-
from django.db.models import Max, Min

from smhouse.models import TermoAdress, TermoPlace, TermoReading

from datetime import datetime, timedelta

from django.conf import settings

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os


def draw_termo_day(slug, ambient, data):
   # output image parameters
    w_h, tab, ax_col, gr_col = [1520, 400], 50, "#333", "#aaa"
   # TermoAdress
    termo = TermoAdress.objects.get(slug = slug)
   # TermoPlaces
    tp = TermoPlace.objects.filter(where = termo, ambient = ambient)

   # get DateTime range & array for x-axis (full hours)
    d_end, d_start = datetime.now(), datetime.now() - timedelta(hours=24)

    next = d_start.replace(microsecond=0, second=0, minute=0) + timedelta(hours=1)
    prev = d_end.replace(microsecond=0, second=0, minute=0)

    hours = [next]
    while hours[-1] != prev:
        next = next + timedelta(hours=1)
        hours.append( next )

   # BACKGROUND IMAGE
    img = Image.new('RGB', w_h, color = '#cecff0')
    draw = ImageDraw.Draw( img )
    draw.line([tab, 10, tab, 370], fill=ax_col, width = 0)
    draw.line([tab, 370, 1490, 370], fill=ax_col, width = 0)

   # draw hours
    for h in hours:
        x = int( round( h.timestamp() - d_start.timestamp() )/60 ) + tab
        draw.line([x, 10, x, 370], fill=gr_col, width = 0)
        draw.text([x-4, 375], str(h.hour), fill=(0,0,0,128))

   # Format y-axis
    min, max = 100, -100
    for t in tp:
        temp = TermoReading.objects.filter(place = t, date__range=[d_start, d_end])

        t_max = temp.aggregate(Max('temp'))
        if float(t_max['temp__max']) >= max:
            max = float(t_max['temp__max'])

        t_min = temp.aggregate(Min('temp'))
        if float(t_min['temp__min']) <= min:
            min = float(t_min['temp__min'])

    y_k = -300/(max - min)

   # Draw y-axis legend
    draw.line([tab, ((max-min)*y_k)+350, 1490, ((max-min)*y_k)+350], fill="#A52A2A", width = 0)
    draw.text([10,  ((max-min)*y_k)+345], str(max), fill=(165,42,42,128))

    draw.line([tab, ((min-min)*y_k)+350, 1490, ((min-min)*y_k)+350], fill="#2a55a5", width = 0)
    draw.text([10,  ((min-min)*y_k)+345], str(min), fill=(42,85,165,128))

    for i in range(1, 5):
        draw.line([tab, ((max-min)*y_k*0.2*i)+350, 1490, ((max-min)*y_k*0.2*i)+350], fill=gr_col, width = 0)
        draw.text([10,  ((max-min)*y_k*0.2*i)+345], str(round( ((max-min)*0.2*i)+min, 1 )), fill=(0,0,0,128))

    img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + slug + '_day_back_' + str(ambient) + '.png' )

   # iterate Graph's
    for t in tp:
       # TermoReaings
        tr = TermoReading.objects.filter(place=t, date__range=[d_start, d_end]).order_by('-date')

       # layer with Transparent backgroung
        img = Image.new('RGBA', w_h, (255, 0, 0, 0))
        draw = ImageDraw.Draw( img )

       # plot reaings data
        for r in tr:
            x = int( round((r.date.timestamp() - d_start.timestamp())/60) ) + tab
            y = ((float(r.temp) - min) * y_k) + 350
            draw.rectangle( [x, y, x+2, y+2], fill=t.color, outline=t.color, width=4 )

       # save image
        img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + t.where.slug + '_day_temp_' + str(t.order) + '.png', 'PNG' )
