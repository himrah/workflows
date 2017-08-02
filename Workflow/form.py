from Workflow.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.forms import Textarea,CharField,TextInput


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


class UserName(User):
    class Meta:
        proxy = True
    def __str__(self):
        return self.first_name+' '+self.last_name


class TaskEditForm(forms.ModelForm):
    assign=forms.ModelChoiceField(queryset=UserName.objects.all())
    class Meta:
        model = Task
        fields = ['name','status','created_date','created_by','task_description','comments','priority','tat','assign']
        widgets ={
            'created_date' : TextInput(attrs={'class':'disabled,form-control'}),
            'name' : TextInput(attrs={'class':'form-control'}),
            'task_description':Textarea(attrs={'class':'form-control'})
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

