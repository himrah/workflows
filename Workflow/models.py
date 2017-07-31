from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.



class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    head = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    description=models.TextField()
    head = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    nothing = '----'
    new ='New'
    inprocess='In Process'
    complete='Complete'
    choices=(
        (new , 'New'),
        (inprocess,'In Process'),
        (complete,'Complete'),
    )

    high='High'
    low='Low'
    normal='Normal'

    p_choice=(
        (high,'High'),
        (low,'Low'),
        (normal,'Normal')
    )


    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    created_date=models.DateTimeField(default=datetime.now,blank=True)
    created_by=models.CharField(max_length=20)
    status=models.CharField(max_length=10,choices=choices,default=nothing)
    task_description=models.TextField()
    comments=models.TextField(blank=True)
    modify_by=models.CharField(max_length=20)
    priority=models.CharField(max_length=10,choices=p_choice,default=nothing)
    tat=models.IntegerField()
    assign=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.id)+' '+self.name



class Email_msg(models.Model):
    id = models.AutoField(primary_key=True)
    sender_id = models.CharField(max_length=20)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.TextField(blank=True)
    content = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.subject

class Inbox(models.Model):
    id = models.AutoField(primary_key=True)
    sender_id = models.CharField(max_length=20,null=True)
    subject = models.CharField(max_length=150,null=True)
    
    #content = models.TextField()
    content = RichTextField()
    receiver_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.subject


class Sent_item(models.Model):
    id = models.AutoField(primary_key=True)
    sender_id = models.CharField(max_length=20)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    subject = models.TextField(blank=True)
    content = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.subject


class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    receiver_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject = models.TextField(blank=True)
    content = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.subject

