from django import forms
from jobs.models import Job,Application

class JobCreationForm(forms.ModelForm):
    
    class Meta():
        model = Job
        exclude = ['change_at','created_by',]

class JobApplicationForm(forms.ModelForm):

    class Meta():
        model = Application
        exclude = ['job','applied_by']