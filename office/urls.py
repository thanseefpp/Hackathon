from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.adminlogin,name='adminlogin'),
    path('admin/user/',views.adminlogout,name='adminlogout'),
    path('admin/dashboard/',views.admindash,name='admindash'),
    path('admin/user/',views.userlist,name='userlist'),
]