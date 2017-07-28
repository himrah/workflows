from django.shortcuts import render,render_to_response
from .models import *
# Create your views here.
def Home(request):
    p=Project.objects.all()
    t=Task.objects.all()
    return render_to_response('home.html',{'project':p,'task':t,'pid':'home'})


def ProjectTask(request,pk):
    p = Project.objects.all()
    pi = Project.objects.get(id=pk)
    t=Task.objects.filter(project_id=pk)
    return render_to_response('home.html',{'project':p,'task':t,'pid':pi})

def TaskDetail(request,pk):
    p = Project.objects.all()
    #pi = Project.objects.get(id=pid)
    t=Task.objects.get(id=pk)
    return render_to_response('home.html',{'task':t,'project':p,'work':'edit'})

def Email(request):
    e = Inbox.objects.all()
    return render_to_response('email.html',{'email':e})

def EmailDetail(request,pk):
    e=Inbox.objects.get(id=pk)
    return render_to_response('email.html',{'mail':e})

from .form import InboxForm

from django.template import RequestContext
def Compose(request):
    form = InboxForm()
    return render(request,'email.html',{'flag':True,'form':form})

from django.http.response import HttpResponse,HttpResponseRedirect


def sending(request):
    if request.method=='POST':
        form=InboxForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.sender_id="Admin"
            f.save()
            return HttpResponseRedirect('/email/')