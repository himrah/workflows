"""WorkFlows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Workflow.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home,name='home'),
    url(r'^project/(?P<pk>.*)',ProjectTask,name='ProjectTask'),
    url(r'^task/(?P<pk>\d+)$',TaskDetail,name='TaskDetail'),
    url(r'^task/(?P<pk>.*)/edit/$',Edit,name='Edit'),
    url(r'^email/$',Email,name='Email'),
    url(r'^email/(?P<pk>\d+)$', EmailDetail, name='ProjectTask'),
    url(r'^compose/',Compose,name='compose'),
    url(r'^reports/',Reports,name='reports'),
    url(r'^api/project_data$',project_data,name='project-data'),
    url(r'^api/project_data/(?P<what>.*)/$',prj_data,name='prj-data'),
    url(r'^sending/',sending,name='sending'),
    url(r'^isread/(?P<pk>\d+)$',Isread,name='isread'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/login/$',login,name='login'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^auth/$',auth_view,name='auth'),
]
