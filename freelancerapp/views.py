from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Job,Application,Applicant,Company
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("Hello Freelancer")
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def job(request):
    postjob=Job.objects.all().values()
    template=loader.get_template('job.html')
    context={
        'postjob': postjob,
    }
    return HttpResponse(template.render(context,request))

def table(request):
    template=loader.get_template('apply.html')
    return HttpResponse(template.render())
def postjob(request):
    template=loader.get_template('postjob.html')
    return HttpResponse(template.render())
def addjob(request):
    a=request.POST['company']
    b=request.POST['start_date']
    c=request.POST['end_date']
    d=request.POST['title']
    e=request.POST['salary']
    f=request.POST['description']
    g=request.POST['experience']
    h=request.POST['location']
    i=request.POST['skills']
    j=request.POST['creation_date']
    job=Job(company=a,start_date=b,end_date=c,title=d,salary=e,description=f,experience=g,location=h,skills=i,creation_date=j)
    job.save()
    return HttpResponseRedirect(reverse('index'))
def application(request):
    application=Application.objects.all().values()
    template=loader.get_template('application.html')
    context={
        'application': application,
    }
    return HttpResponse(template.render(context,request))
def applicant(request):
    applicant=Applicant.objects.all().values()
    template=loader.get_template('applicant.html')
    context={
        'applicant': applicant,
    }
    return HttpResponse(template.render(context,request))
def company(request):
    company=Company.objects.all().values()
    template=loader.get_template('company.html')
    context={
        'company': company,
    }
    return HttpResponse(template.render(context,request))
def homepage(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render({},request))
def loginFreelancer(request):
    template=loader.get_template('intax.html')
    return HttpResponse(template.render())
def loginHired(request):
    template=loader.get_template('intex3.html')
    return HttpResponse(template.render())