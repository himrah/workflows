from rest_framework import serializers
from Workflow.models import *
from django.contrib.auth.models import User, Group
from rest_framework.reverse import  reverse
from django.contrib.auth.models import User
from .form import UserName,UserFullName



from django import forms
#assign=forms.ModelChoiceField(queryset=UserFullName.objects.all())

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')


class Taskserializer(serializers.HyperlinkedModelSerializer):
    assign=forms.ModelChoiceField(queryset=UserName.objects.all())
    class Meta:
        model = Task
        fields = ('id','name','created_date','created_by','status','comments','modify_by','priority','tat','assign')


class ProjectSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields=('id','name','task_set','description')

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

        