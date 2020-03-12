# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict

from jobs.models import Jobs

# JSON
from django.http import JsonResponse
#from django.core import serializers


from jobs.views import jobs_main


# JOB JSON BY ID
def json_id(request, job_id):
    args = jobs_main.default(request)

#    job = {}
# RESTRICT ACCESS
    if args['u_job_list'] == False:
#        serialized_job = serializers.serialize('json', [ Jobs.objects.none(), ])
#        job = Jobs.objects.none()
        job = model_to_dict( Jobs.objects.none() )
    else:
#        serialized_job = serializers.serialize('json', [ Jobs.objects.get( id = job_id ), ])
#        job = Jobs.objects.get( id = job_id )
        job = model_to_dict( Jobs.objects.get( id = job_id ) )

    import json
    serialized = json.dumps( job )
#    return JsonResponse( serialized_job, safe=False )
    return JsonResponse( serialized )
