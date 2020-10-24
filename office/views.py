from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import *
from django.core.files import File
# Create your views here.

def adminlogin(request):
    if request.user.is_superuser:
        return redirect('admindash')

    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
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
        resume = Resumes.objects.all()
        return render(request,'admindash.html',{'resume':resume})
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

