from django.urls import path

from users import views

urlpatterns = [
    path('singup/',views.sinup,name='signup'),
    path('register_student/',views.register_student,name='register_student'),
    path('register_employer/',views.register_employer,name='register_employer'),
]
    