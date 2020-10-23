from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.

def adminlogin(request):
    if request.user.is_superuser:
        return redirect('admindash')

    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request.user)
            return redirect('admindash')

        else:
            messages.error(request, "😢 Wrong username/password!")
            return redirect(adminlogin)
    else:
        return render(request,'admin.html')



def admindash(request):
    if request.user.is_superuser:
        return render(request,'admindash.html')
    else:
        return redirect(adminlogin)

def adminlogout(request):
    auth.logout(request)
    return redirect(adminlogin)


def userlist(request):
    return render(request,'userlist.html')