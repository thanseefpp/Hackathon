from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import JsonResponse
import json
import requests
from django.contrib import messages
from django.views.generic import View


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
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LfWINsZAAAAAPjbqASGnDDad7sTnIA92xzau9TW"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return HttpResponseRedirect("/")

        userinfo.save()
        return render(request,'success.html')

    else:
        return render(request,'home.html')



# def mobile(request):
#     data = json.loads(request.body)
#     number=data['mobile']

#     url = "https://d7networks.com/api/verifier/send"
#     number=str(91) + number
    
#     payload = {'mobile': number,
#     'sender_id': 'SMSINFO',
#     'message': 'Your otp code is {code}',
#     'expiry': '900'}
#     files = [

#     ]
#     headers = {
#     'Authorization': 'Token 0d21f1e3cb977b24ebd925ec71d3fec0cb0a41f3'
#     }

#     response = requests.request("POST", url, headers=headers, data = payload, files = files)

#     print(response.text.encode('utf8'))
#     data=response.text.encode('utf8')
#     datadict=json.loads(data.decode('utf-8'))

#     id=datadict['otp_id']
#     status=datadict['status']
#     print('id:',id)
#     request.session['id'] = id

#     return JsonResponse("otp send",safe=False)




    # url = "https://d7networks.com/api/verifier/send"
    # number=str(91)+ number

    # payload = {'mobile': number,
    # 'sender_id': 'SMSINFO',
    # 'message': 'Your otp code is {code}',
    # 'expiry': '900'}
    # files = [

    # ]
    # headers = {
    # 'Authorization': 'Token 0d21f1e3cb977b24ebd925ec71d3fec0cb0a41f3'
    # }

    # response = requests.request("POST", url, headers=headers, data = payload, files = files)

    # print(response.text.encode('utf8'))
    # data=response.text.encode('utf8')
    # datadict=json.loads(data.decode('utf-8'))

    # id=datadict['otp_id']
    # status=datadict['status']
    # print('id:',id)
    # request.session['id'] = id



# index 
#         otp = request.POST['otp']

#         id = request.session['id']
#         url = "https://d7networks.com/api/verifier/verify"

#         payload = {'otp_id': id,
#         'otp_code': otp}
#         files = [

#         ]
#         headers = {
#         'Authorization': 'Token 0d21f1e3cb977b24ebd925ec71d3fec0cb0a41f3'
#         }

#         response = requests.request("POST", url, headers=headers, data = payload, files = files)


#         print(response.text.encode('utf8'))

#         print(response.text.encode('utf8'))
#         data=response.text.encode('utf8')
#         datadict=json.loads(data.decode('utf-8'))
#         print('check datadict :',datadict)
#         status=datadict['status']
