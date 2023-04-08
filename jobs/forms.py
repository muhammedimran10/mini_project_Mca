from django import forms
from jobs.models import Job

class JobCreationForm(forms.ModelForm):
    
    class Meta():
        model = Job
        exclude = ['change_at','created_by',]