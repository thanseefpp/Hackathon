from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.adminlogin,name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('admin/dashboard/',views.admindash,name='admindash'),
    path('admin/user/',views.userlist,name='userlist'),
    path('admin//shortlist',views.shortlist,name='shortlist'),
]