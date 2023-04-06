from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout

from users.models import Userprofile
from users.forms import UserRegistrationForm,CompanyCreationForm
from jobs.models import Company
# Create your views here.

def sinup(request):
    return render(request,'users/signup.html')


def register_student(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile= Userprofile.objects.create(user=user)
            userprofile.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register_student.html',{'form':form})



def register_employer(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form2 = CompanyCreationForm(request.POST)

        if form.is_valid():

            if form2.is_valid():
                user = form.save()

                # company_name = request.POST.get('company_name')
                # company_addres = request.POST.get('company_addres')
                # company_zipcode = request.POST.get('company_zipcode')
                # company_place = request.POST.get('company_place')

                # company= Company.objects.create(
                #     user=user,
                #     company_name=company_name,
                #     company_addres=company_addres,
                #     company_zipcode=company_zipcode,
                #     company_place=company_place
                #     )

                company = form2.save(commit=False)
                company.user = user
                company.save()
        
                userprofile= Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
                return redirect('home')
        
    else:
        form = UserRegistrationForm()
        form2 = CompanyCreationForm()
    return render(request,'users/register_employer.html',{'form':form,'form2':form2})





# def register_employer(request):

#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             account_type = request.POST.get('account_type','student')
            
#             if account_type == 'employer':
#                 userprofile= Userprofile.objects.create(user=user, is_employer=True)
#                 userprofile.save()
#             else:
#                 userprofile= Userprofile.objects.create(user=user)
#                 userprofile.save()
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request,'users/register_employer.html',{'form':form})