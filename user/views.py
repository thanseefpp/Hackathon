from django.shortcuts import render,redirect
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from .models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        job_type = request.POST['job_type']
        experiance = request.POST['experiance']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        notice = request.POST['notice']
        salary = request.POST['salary']
        resume = request.FILES.get('resume')
        userinfo = Resumes(expected_salary=salary,notice_period=notice,gender_type=gender,full_name=fullname,job_type=job_type,year_of_experiance=experiance,dob=date_of_birth,resume=resume)
        userinfo.save()
        return render(request,'success.html')
    else:
        return render(request,'home.html')
