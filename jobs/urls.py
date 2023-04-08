from django.urls import path
from jobs import views


urlpatterns = [
    path('',views.home,name='home'),
    path('my_jobs',views.my_jobs,name='my_jobs'),

    path('add_job',views.add_job,name='add_job'),
    path('<int:job_id>/edit/',views.edit_job,name='edit_job'),

]