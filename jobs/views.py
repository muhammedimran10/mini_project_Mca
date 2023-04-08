from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from jobs.models import Job
from jobs.forms import JobCreationForm
@login_required()
def home(request):

    jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:5]

    return render(request,'jobs/home.html',{'jobs':jobs})

def my_jobs(request):
    jobs = Job.objects.filter(created_by=request.user).order_by('-created_at')[0:5]

    return render(request,'jobs/my_jobs.html',{'jobs':jobs})

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
