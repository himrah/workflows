from django.shortcuts import render,render_to_response,get_object_or_404
from .models import *
from .form import *
from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.



#line_chart = TemplateView.as_view(template_name='reports.html')
#line_chart_json = LineChartJSONView.as_view()



def Home(request):
    p=Project.objects.all()
    t=Task.objects.all()
    return render_to_response('home.html',{'project':p,'task':t,'pid':'home'})



def prj_data(request,what):
    
    if what == 'priority':
        l_count=Task.objects.filter(priority='Low').count()
        h_count=Task.objects.filter(priority='High').count()
        n_count=Task.objects.filter(priority='Normal').count()
        
        label=['Hight','Low','Normal']
        count=[h_count,l_count,n_count]
        data={
            'label':label,
            'count':count
        }
        return JsonResponse(data)
    elif what == 'status':
        c_count=Task.objects.filter(status='Complete').count()
        i_count=Task.objects.filter(status='In Process').count()
        n_count=Task.objects.filter(status='New').count()
        label=['Complete','In Process','New']
        count=[c_count,i_count,n_count]
        data={
            'label':label,
            'count':count
        }
        return JsonResponse(data)

    #p=Project.objects.filter()

def project_data(request):
    p=Project.objects.all()
    project=[i.name for i in p]
    print(project)
    count=[p[0].task_set.count(),p[1].task_set.count(),p[2].task_set.count()]
    data={
        'project':project,
        'count':count
    }
    return JsonResponse(data)


def Reports(request):
    
    #p=Project.objects.all()
    #project=[i.name for i in p]
    #print(project)
    #count=[p[0].task_set.count(),p[1].task_set.count(),p[2].task_set.count()]
    #['CMS', 'Scraping', 'Audit']
    #data = ModelDataSource(p,fields=['name'])
    #chart=flot.LineChart(data)
    return render_to_response('reports.html')
 #   line_chart = TemplateView.as_view(template_name='reports.html')
 #   line_chart_json = LineChartJSONView.as_view()
#    return HttpResponse(line_chart_json)

def Edit(request,pk):
    #form=TaskEditForm()
    task=get_object_or_404(Task,id=pk)
    form=TaskEditForm(request.POST or None,instance=task)
    user=request.user
    if request.POST and form.is_valid():
        name=request.user.first_name+" "+request.user.last_name
        task.modify_by=name
        task.save()
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'home.html',{'form':form,'work':'taskedit'})


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