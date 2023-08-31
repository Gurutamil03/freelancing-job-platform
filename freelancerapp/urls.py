from django.urls import path
from . import views

urlpatterns=[
    path('view/',views.index),
    path('loginfreelancer/',views.loginFreelancer,name='intexlogin'),
    path('loginHired/',views.loginHired,name='intexlogin1'),
    path('home/',views.home,name='home'),
    path('jobtable/',views.job),
    path('applyform/',views.table,name='apply'),
    path('postjobform/',views.postjob,name='postjob'),
    path('postjob/addjob',views.addjob),
    path('applicationtable/',views.application),
    path('applicanttable/',views.applicant),
    path('companytable/',views.company)   
]
