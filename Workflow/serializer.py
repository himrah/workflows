from rest_framework import serializers
from Workflow.models import *
from django.contrib.auth.models import User, Group, Permission,ContentType
from rest_framework.reverse import  reverse
from django.contrib.auth.models import User
from .form import UserName,UserFullName,Alluser



from django import forms
#assign=forms.ModelChoiceField(queryset=UserFullName.objects.all())


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #user_permissions = PermissionSerializer()
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','inbox_set','user_permissions')


import json
class Taskserializer(serializers.HyperlinkedModelSerializer):
    assign_name = serializers.CharField(source='assign.get_full_name',required=False)
    #assign_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True)
    #assign_id = serializers.SlugRelatedField(slug_field='id')
    #assign = serializers.ChoiceField(choices=UserName.objects.all())
    #assign=forms.ModelChoiceField(queryset=UserName.objects.all())
    #assign = serializers.ChoiceField(choices=({'sdf':'sdf'}))
    class Meta:
        model = Task
        fields = ('id','name','created_date','created_by','status','task_description','comments','modify_by','priority','tat','assign_name','assign')



class ProjectSeralizer(serializers.HyperlinkedModelSerializer):
#    task_set = Taskserializer(many=True)
    task_set = Taskserializer(required=False,many=True)
    class Meta:
        model = Project
        fields=('id','name','description','head','task_set')

class SentItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sent_item
        fields = ('id','subject','content','sender_id','receiver_id','date','is_read')



class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    project_set = ProjectSeralizer(required=False,many=True)
    class Meta:
        model = Department
        fields = ('id','name','head','project_set')


class InboxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inbox
        fields = ('id','subject','content','sender_id','receiver_id','is_read','date')

class ContentTypeSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType
        fields = ('id','app_label','model')

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    #content_type = ContentTypeSerialzier(many=True,)
    class Meta:
        model = Permission
        fields = ('id','content_type','codename','name')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name','user_set')




"""class Departmentserializer(serializers.HyperlinkedModelSerializer):
    head = Userserializer()
    class Meta:
        model = Department
        fields = ('id','name','head')"""


"""
class UserName_serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name')

class Taskserializer(serializers.HyperlinkedModelSerializer):
    #created_by = UserName_serializers()
    #assign=forms.ModelChoiceField(queryset=UserName.objects.all())
    assign = forms.ModelChoiceField(queryset=UserFullName())

#    created_by = UserName_serializers()
    class Meta:
        model = Task
        fields = ('id','name','created_date','created_by','modify_by','priority','status','comments','tat','assign')


class Emailserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email_msg
        fields = '__all__' 

class Groupserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class Userserializer(serializers.HyperlinkedModelSerializer):
    #email_msg = serializers.HyperlinkedIdentityField(view_name="myapp:user-detail")
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name')


class Departmentserializer(serializers.HyperlinkedModelSerializer):
    head = Userserializer()
    class Meta:
        model = Department
        fields = ('id','name','head')        




class Projectserializer(serializers.HyperlinkedModelSerializer):
    #head = Departmentserializer()
    #head = serializers.HyperlinkedIdentityField(view_name="api:department-list")
#    task_set = Taskserializer()
#    task_set = serializers.HyperlinkedIdentityField(view_name="task-list",lookup_field = 'name',many=True)
    #task_set  forms.ModelChoiceField(queryset=UserFullName.objects.all())
    head = Departmentserializer()
    task_set = Taskserializer(many=True,)
    class Meta:
        model = Project
        fields = ('id','name','description','head','task_set')




#task = Taskserializer()
#assign = Userserializer()
#head = Userserializer()
#project_id = Projectserializer()
#email_msg = Emailserializer()
#task = Taskserializer()
#group = Groupserializer()"""

        