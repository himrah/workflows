from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from django.contrib.auth.models import Use
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



"""class Profile(User):
    class Meta:
        proxy = True
        ordering = (first_name,)

        def last_seen(self):
                return cache.get('seen_%s' % user.username)

        def online(self):
            if self.last_seen():
                now = datetime.datetime.now()
                if now > self.last_seen() + datetime.timedelta(
                                seconds=settings.USER_ONLINE_TIMEOUT):
                    return False
                else:
                    return True
            else:
                return False       """ 


def upload_path_handler(instance, filename):
    #return "user_{id}/{file}".format(id=instance.user.id, file=filename)
    return "photos/{t}".format(t)


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
    created_date=models.DateTimeField(default=datetime.now,null=True)
    created_by=models.CharField(max_length=20,blank=True,null=True)
    status=models.CharField(max_length=10,choices=choices,default=nothing)
    task_description=models.TextField()
    comments=models.TextField(blank=True)
    modify_by=models.CharField(max_length=20,blank=True)
    priority=models.CharField(max_length=10,choices=p_choice,default=nothing)
    tat=models.IntegerField()
    #file=models.ImageField(upload_to='photos/%d/',blank=True,null=True)
    #file=models.ImageField(upload_to=upload_path_handler, blank=True,null=True)
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
    content = RichTextField()
    is_read = models.BooleanField(default=True)
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



