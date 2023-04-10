from django.db import models
from users.models import User
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User,related_name='company',on_delete=models.CASCADE)
    company_name = models.CharField(max_length=225)
    company_addres = models.CharField(max_length=225,blank=True, null=True)
    company_zipcode = models.CharField(max_length=225,blank=True, null=True)
    company_place = models.CharField(max_length=225,blank=True, null=True)

    def __str__(self):
        return self.company_name


class Job(models.Model):

    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EMPLOYED ,'Employed'),
        (ARCHIVED ,'Archived')
    )

    title = models.CharField(max_length=225)
    short_description = models.TextField()
    long_description = models.TextField(blank=True,null=True)
    
    created_by = models.ForeignKey(User,related_name='jobs',on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20,choices=CHOICES_STATUS,default=ACTIVE)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job,related_name='applications',on_delete=models.CASCADE)
    content= models.TextField(default="")
    experience= models.TextField()
    applied_by = models.ForeignKey(User,related_name='applications',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ConversationMessages(models.Model):
    application = models.ForeignKey(Application,related_name="conversitionmessages",on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name="conversitionmessages",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']