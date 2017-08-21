from rest_framework import serializers
from Workflow.models import *
from django.contrib.auth.models import User, Group
from rest_framework.reverse import  reverse
from django.contrib.auth.models import User


class Projectserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

"""class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Taskserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Emailserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email_msg
        fields = '__all__'   """            