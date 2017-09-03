from Workflow.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.forms import Textarea,CharField,TextInput,ChoiceField


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password','type':'password'}))

    def clean(self,*args,**kwargs):
        username =self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("this user doest not exist")
        return super(LoginForm,self).clean(*args,**kwargs)







class UserMail(User):
    class Meta:
        proxy = True
    def __str__(self):
        return self.first_name+'<'+self.email+'>'


class UserFullName(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()


class UserName(User):
    class Meta:
        proxy = True
    def __str__(self):
        return self.first_name+' '+self.last_name

import json
def Alluser(User):
    dic={}
    user=User.objects.all()
    for i in user:
        dic.update({i.get_full_name():str(i.id)})
        #dict.update({'name':i.get_full_name})
    return json.loads(json.dumps(dic))


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        head = forms.ModelChoiceField(queryset=UserName.objects.all())
        fields = ('name','description','head')
        widgets = {
            'name':TextInput(attrs={'class':'form-ctr'}),
            'description':Textarea(attrs={'class':'form-control'}),
            'head':forms.Select(attrs={'class':'form-ctr'})
        }


class TaskEditForm(forms.ModelForm):
    assign=forms.ModelChoiceField(UserName.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['name','status','created_date','created_by','task_description','comments','priority','tat','assign']
        widgets ={
#            'created_date' : TextInput(attrs={'class':'form-control','disabled':'true'}),
            'created_by' : TextInput(attrs={'class':'form-control'}),
            'created_date' : TextInput(attrs={'class':'form-control'}),

            'name' : TextInput(attrs={'class':'form-control'}),
            'task_description':Textarea(attrs={'class':'form-control','style':'height: 3cm !important;overflow: hidden;max-width:100%;min-width:100%'}),#,style="height: 30px !important;overflow: hidden;resize: none;"
            'comments':Textarea(attrs={'class':'form-control','style':'height: 3cm !important;overflow: hidden;max-width:100%;min-width:100%'}),
            'priority':forms.Select(attrs={'class':'form-control'}),
            'tat':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'assign':forms.Select(attrs={'class':'form-control'}),
            #'assign':CharField(attrs={'class':'form-control'}),
            #,widget=forms.Select(attrs={'class':'hidden'})
        }





class InboxForm(forms.ModelForm):
    content = Inbox
    content = forms.CharField(widget=CKEditorWidget())
    receiver_id=forms.ModelChoiceField(queryset=UserMail.objects.all())
    #subject = CharField(widget={'class':'subject'})
    class Meta:
        model= Inbox
        fields=['subject','content','receiver_id']
        widgets={
            'content' : Textarea(attrs={'class':'texarea'}),
            'subject' : TextInput(attrs={'class':'subject'})
        }

class SentForm(forms.ModelForm):
    #content = Sent_item
    receiver_id=forms.ModelChoiceField(queryset=UserMail.objects.all())
    class Meta:
        model = Sent_item
        fields = ['subject','content','receiver_id']

