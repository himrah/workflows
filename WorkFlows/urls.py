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
from django.contrib.auth.views import logout,login
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework.authtoken import views as authtoken_views
from Workflow.views import *    
from rest_framework import routers



router=routers.DefaultRouter()
#router=routers.DefaultRouter()
#router.register('task',TaskSet.as_view({'put':'update','post':'post'}))
router.register('task',TaskSet)
router.register('project',ProjectSet)
router.register('user',UserSet)
router.register('department',DepartmentSet)
router.register('inbox',InboxSet)
router.register('sent',SentItemset)
router.register('group',GroupSet)
#router.register('contenttype',ContentTypeSet)
router.register('permission',PermissionSet)
#router.register('task',Taskset,)
#router.register('user',Userset,'user-detail')
#router.register('department',Departmentset)
#router.register('project',Projectset)

#router.register('project',Projectset)

urlpatterns = [
#    url(r'^api/',include('rest_framework.urls',namespace='rest_framework'))
    url(r'^api/',include(router.urls)),
#    url(r'^api/task/',TaskSet.as_view({'put':'update','post':'post','get':'get'})),
    #url(r'^api/user/',UserSet.as_view({'get':'get'})),    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^accounts/logout/$',Logout,name='logout'),
#    url(r'^accounts/logout/',logout,{'template_name':'registration/logout.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home_rest,name='home'),
    url(r'^alert/$',Alert,name='alert'),
    url(r'^rest/',include('Workflow.url',namespace='rest-workflow')),
    url(r'^project/(?P<pk>\d+)/$',ProjectTask,name='ProjectTask'),
    url(r'^create/project$',CreateProject,name='crateproject'),
    url(r'^task/(?P<pk>\d+)$',TaskDetail,name='TaskDetail'),
    url(r'^task/(?P<pk>.*)/edit/$',Edit,name='Edit'),
    url(r'^email/$',Email,name='Email'),
    url(r'^email/(?P<pk>\d+)$', EmailDetail, name='ProjectTask'),
    url(r'^compose/',Compose,name='compose'),
    url(r'^reports/',Reports,name='reports'),
    url(r'^api/project_data$',project_data,name='project-data'),
    url(r'^api/project_data/(?P<what>.*)/$',prj_data,name='prj-data'),
    url(r'^api/single_project/(?P<project>.*)/$',Single,name='single-project'),
    url(r'^api/task_by_emp/(?P<name>.*)/$',task_by_emp,name='emp-task'),
    url(r'^api/project_by_department/(?P<name>.*)/$',prj_by_dpt,name='prj-by-dpt'),
    url(r'^api/employee/$',emp_data,name='emp-data'),
    url(r'^sending/',sending,name='sending'),
    url(r'^sent/$',SentView,name='sent-view'),
    url(r'^sent/(?P<pk>\d+)/$',SentItem,name='sent-item'),
    url(r'^project/create/$',CreateProject,name='create-project'),
    url(r'^isread/(?P<pk>\d+)$',Isread,name='isread'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/login/$',login,name='login'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^auth/$',auth_view,name='auth'),
    url(r'^accounts/profile/',profile,name='profile'),
    url(r'^get_auth_token/$', authtoken_views.obtain_auth_token, name='get_auth_token'),
    url(r'^search/(?P<srchkey>.*)/$',Searching,name='search'),
    url(r'^export/$',export_csv,name='csv'),

]
