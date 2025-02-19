from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import *
from django.core.files import File
import requests
from django.http import JsonResponse
import json
# Create your views here.

def adminlogin(request):
    if request.user.is_superuser:
        return redirect('admindash')

    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LfWINsZAAAAAPjbqASGnDDad7sTnIA92xzau9TW"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return HttpResponseRedirect("/admin/")

        if user:
            login(request,user)
            return redirect('admindash')

        else:
            messages.error(request, "😢 Wrong username/password!")
            return redirect(adminlogin)
    else:
        return render(request,'admin.html')



def admindash(request):
    if request.user.is_superuser:
        resumecount = Resumes.objects.all().count()
        pythondeveloper = Resumes.objects.filter(job_type='Python Developer').count()
        godeveloper = Resumes.objects.filter(job_type='GO Developer').count()
        webdeveloper = Resumes.objects.filter(job_type='Web Developer').count()
        context = {'resumecount':resumecount,'pythondeveloper':pythondeveloper,'webdeveloper':webdeveloper,'godeveloper':godeveloper}
        return render(request,'admindash.html',context)
    else:
        return redirect(adminlogin)

def adminlogout(request):
    auth.logout(request)
    return redirect(adminlogin)


def userlist(request):
    if request.user.is_superuser:
        resume = Resumes.objects.filter(status='Pending')
        return render(request,'userlist.html',{'resume':resume})
    else:
        return redirect(adminlogin)
    

def shortlist(request):
    if request.user.is_superuser:
        resume = Resumes.objects.filter(status='shortlist')
        return render(request,'shortlist.html',{'resume':resume})
    else:
        return redirect(adminlogin)
    

def approve(request,id):
    if request.user.is_superuser:
        resume = Resumes.objects.get(id=id)
        resume.status = 'shortlist'
        resume.save()
        return redirect(userlist)
    else:
        return redirect(adminlogin)

