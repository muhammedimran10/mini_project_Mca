from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

from jobs.models import Job,Application,ConversationMessages

from jobs.forms import JobCreationForm,JobApplicationForm


@login_required()
def home(request):

    jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:5]

    return render(request,'jobs/home.html',{'jobs':jobs})



def add_job(request):
    form = JobCreationForm()
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.created_by=request.user
            job.save()
        return redirect('home')
    return render(request,'jobs/add_job.html',{'form':form})

def edit_job(request, job_id):
    
    ob = get_object_or_404(Job, pk=job_id, created_by=request.user)
    form = JobCreationForm(instance=ob)
    if request.method == 'POST':
        form = JobCreationForm(request.POST, instance=ob)

        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'jobs/edit_job.html',{'form':form})

def applay_for_job(requst,job_id):
    job = Job.objects.get(pk=job_id)
    form = JobApplicationForm()
    if requst.method == 'POST':
        form = JobApplicationForm(requst.POST)

        if form.is_valid():
            application=form.save(commit=False)
            application.applied_by=requst.user
            application.job=job
            application.save()
            return redirect('home')
    return render(requst,'jobs/applay_for_job.html',{'form':form})

def my_jobs(request):
    jobs = Job.objects.filter(created_by=request.user).order_by('-created_at')

    return render(request,'jobs/my_jobs.html',{'jobs':jobs})

def my_applications(request):

    application = Application.objects.filter(applied_by=request.user).order_by('-created_at')
    return render(request,'jobs/my_jobs.html',{'application':application})


def applications(request, job_id):
    application = Application.objects.filter(job_id=job_id).order_by('-created_at')
    return render(request,'jobs/applications.html',{'applications':application})

def view_application(request,application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application,pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application,pk=application_id, applied_by=request.user)

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            conversationmessage = ConversationMessages.objects.create(application=application,content=content, created_by=request.user)
            # create_notification(request,application.cr_by, 'message', extra_id=application.id)
            return redirect('view_application',application_id=application_id)
    return render(request,'jobs/view_application.html',{'application':application})



# def view_application(request, application_id):
#     if request.user.userprofile.is_employer:
#         application = get_object_or_404(aplication,pk=application_id, job__cr_by=request.user)
#     else:
#         application = get_object_or_404(aplication,pk=application_id, cr_by=request.user)

#     if request.method == "POST":
#         content = request.POST.get('content')
#         if content:
#             conversationmessage = ConversationMessages.objects.create(application=application,content=content, cr_by=request.user)
#             create_notification(request,application.cr_by, 'message', extra_id=application.id)
#             return redirect('view_application',application_id=application_id)
#     return render(request,'userprofile/view_application.html',{'application':application})