# -*- coding: utf-8 -*-
from django.contrib import admin
from jobs.models import Jobs, JobObj, JobObj_image, JobObj_file

# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    fields = ['jobs_date_added', 'jobs_date_start', 'jobs_date_done', 'jobs_descr',
              'jobs_zone', 'jobs_type', 'jobs_done', 'jobs_cancel', 'jobs_user',
              'marked', 'marked_id', 'marked_until',
             ]

    list_filter = ['marked', 'jobs_date_added',
                   'jobs_user', 'jobs_zone',
                   'jobs_type', 'jobs_done', 'jobs_cancel',
                  ]

    list_display = ['jobs_date_added', 'jobs_descr_short', 'jobs_zone', #'jobs_type',
                    'jobs_date_start', #'jobs_date_done',
#                    'jobs_done', 'jobs_cancel', 'marked',
                    'marked_id', 'marked_until', #'jobs_user'
                   ]


class JobObjAdmin(admin.ModelAdmin):
    fields = ['obj_added', 'obj_nr', 'obj_title', 'obj_descr', 'obj_actual', 'obj_zone', 'obj_url']

    list_filter = ['obj_added', 'obj_actual', 'obj_zone']

    list_display = ['obj_added', 'obj_nr', 'obj_title', 'obj_descr', 'obj_url', 'obj_actual', 'obj_zone']


admin.site.register(Jobs, JobsAdmin)
admin.site.register(JobObj, JobObjAdmin)

admin.site.register(JobObj_image)
admin.site.register(JobObj_file)
