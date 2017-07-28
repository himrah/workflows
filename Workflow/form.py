from Workflow.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea,CharField,TextInput

class UserMail(User):
    class Meta:
        proxy = True
    def __str__(self):
        return self.first_name+'<'+self.email+'>'


class InboxForm(forms.ModelForm):
    content = Inbox
    receiver_id=forms.ModelChoiceField(queryset=UserMail.objects.all())
    #subject = CharField(widget={'class':'subject'})
    class Meta:
        model= Inbox
        fields=['subject','content','receiver_id']
        widgets={
            'content' : Textarea(attrs={'class':'texarea'}),
            'subject' : TextInput(attrs={'class':'subject'})
        }