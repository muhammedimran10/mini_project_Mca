from django.urls import path
from jobs import views


urlpatterns = [
    path('',views.home,name='home'),
    path('my_jobs',views.my_jobs,name='my_jobs'),

    path('add_job',views.add_job,name='add_job'),
    path('<int:job_id>/edit/',views.edit_job,name='edit_job'),
    path('<int:job_id>/applay_for_job/',views.applay_for_job,name='applay_for_job'),
    path('my_applications/',views.my_applications,name='my_applications'),

    path('applications/<int:job_id>/',views.applications,name="applications"),
    path('view_application/<int:application_id>/',views.view_application,name="view_application"),
]