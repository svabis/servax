# -*- coding: utf-8 -*-
from django.urls import path

from jobs import views

urlpatterns = [
# ===========================================================
# "OBJECT SIZE" CHAPTER
    path(r'objects/', views.obj_list),
#    url(r'^objects/add$', 'jobs.views.obj_add'),

# ===========================================================
# JSON
#    url(r'^j/(?P<job_id>\d+)/$', views.json_id),



# ===========================================================
# MARKED JOBS LIST
    path('m_order/', views.marked_reorder), # ORDER DRAG'N'DROP
    path('marked/', views.marked, name='marked_job_list'),
    path('mark/', views.marking),
    path('unmark/', views.unmarking),

# ===========================================================
# JOBS TO DO LIST
    path('to_do/<int:sort_id>/', views.to_do),
    path('to_do/', views.to_do, name='main_job_list'),

# JOB START
    path('start/<int:job_id>/', views.job_start),
# JOB FINISHED
    path('finish/<int:job_id>/', views.job_finish),
# JOB CANCEL
    path('cancel/<int:job_id>/', views.job_cancel),

# ===========================================================
# CANCELED JOBS LIST
    path('canceled/<int:sort_id>/', views.canceled),
    path('canceled/', views.canceled),

# ===========================================================
# FINISHED JOB LIST
    path('done/<int:sort_id>/', views.done),
    path('done/', views.done),

# ===========================================================
# ADD JOB
    path('add/', views.add, name='job_add'),

# ===========================================================
# MAIN --> JOBS TO DO LIST
    path('', views.jobs_main, name='menu_job'),
]
