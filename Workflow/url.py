from django.conf.urls import include, url
from .models import *
from rest_framework import serializers
from .views import *
from django.contrib.auth.models import *


urlpatterns = [
    url(r'^$',Home_rest,name='home'),
    url(r'^email',Email_rest,name='rest-email'),
]    

"""class Departmentset(serializers.HyperlinkedModelSerializer):
    head = serializers.HyperlinkedIdentityField(view_name="Workflow:user-list")
    class Meta:
        model = Department
        fields = ('id','name','head')
        #fields = ('id','username','first_name','last_name','email','groups')"""