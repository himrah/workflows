from django.conf.urls import include, url
from .models import *
from rest_framework import serializers

from django.contrib.auth.models import *



class Departmentset(serializers.HyperlinkedModelSerializer):
    head = serializers.HyperlinkedIdentityField(view_name="Workflow:user-list")
    class Meta:
        model = Department
        fields = ('id','name','head')
        #fields = ('id','username','first_name','last_name','email','groups')