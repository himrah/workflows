from django.shortcuts import render,render_to_response
from .models import *
from .form import *
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
def Home(request):
    p=Project.objects.all()
    t=Task.objects.all()
    return render_to_response('home.html',{'project':p,'task':t,'pid':'home'})


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form=LoginForm()
        c={'form':form}
        c.update(csrf(request))
        return render(request,'registration/login.html',c)

def logout(request):
    auth.logout(request)
    return render_to_response('registration/logged_out.html')

def auth_view(request):
    if request.method=='POST':
        response_data={}
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        u=User.objects.filter(username=username)
        if not u:
            return HttpResponse('username')
        if user is not None:
            auth.login(request, user)
#            response_data['result'] = 'Success'
#            response_data['message'] = 'you are login'
            #return HttpResponse(json.dumps(response_data),content_type="application/json")
            return HttpResponseRedirect('/')
        elif request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:


#            form = LoginForm(request.POST)
#            c = {'form': form}
#            c.update(csrf(request))
 #           response_data['result'] = 'fail'
  #          response_data['message'] = 'do not'
            return HttpResponse('not')
            #return HttpResponse(json.dumps(response_data),content_type="application/json")

            #return render(request, 'registration/login.html', c)"""""            



def Isread(request,pk):
    e = Inbox.objects.get(id=pk)
    e.is_read = True
    e.save()
    return HttpResponse('OK')

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
    return render(request,'email.html',{'email':e,'inbox':True})

def EmailDetail(request,pk):
    e=Inbox.objects.get(id=pk)
    return render_to_response('email.html',{'mail':e,'inbox':True})

from .form import InboxForm

from django.template import RequestContext
def Compose(request):
    form = InboxForm()
    return render(request,'email.html',{'compose':True,'form':form})

from django.http.response import HttpResponse,HttpResponseRedirect




def sending(request):
    if request.method=='POST':
        form=InboxForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.sender_id="Admin"
            f.save()
            return HttpResponseRedirect('/email/')