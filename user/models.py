from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Resumes(models.Model):
    full_name = models.CharField(max_length = 200, null =True)
    job_type = models.CharField(max_length = 200, null =True)
    year_of_experiance = models.CharField(max_length = 200, null=True)
    dob = models.DateField(null=True)
    resume=models.FileField(null=True,blank=True)
    gender_type = models.CharField(max_length =200,null=True)
    notice_period = models.IntegerField(default=0,null=True,blank=True)
    expected_salary = models.IntegerField(default=0,null=True,blank=True)
    status = models.CharField(default='Pending',max_length =200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    mobile = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return str(self.id)

