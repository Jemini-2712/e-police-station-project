from django.db import models
from citizen.models import *

# Create your models here.

class Commissioner(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=50)
    stationname = models.CharField(max_length=40)
    action = models.BooleanField(default=False)


    def __str__(self):
        return self.email

class Fir(models.Model):
    
    pname = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    cname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    address = models.TextField()
    fir = models.TextField()
    status = models.BooleanField(default=False)
    solved_by = models.ForeignKey(Commissioner,on_delete=models.SET_NULL,blank=True,null=True)
    pic = models.FileField(upload_to='photo',null=True,blank=True) 


    def __str__(self):
        return self.pname.uname

class Complaint(models.Model):
    
    cpname = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    ccname = models.CharField(max_length=50)
    cphone = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    caddress = models.TextField()
    complaint = models.TextField()
    cstatus = models.BooleanField(default=False)
    solvedby = models.ForeignKey(Commissioner,on_delete=models.SET_NULL,blank=True,null=True)
    picture = models.FileField(upload_to='photo',null=True,blank=True) 


    def __str__(self):
        return self.cpname.uname

class Inspector(models.Model):
    
    iemail = models.EmailField(unique=True)
    ipassowrd = models.CharField(max_length=30)
    iname = models.CharField(max_length=50)
    iphone = models.CharField(max_length=15)
    iarea = models.CharField(max_length=50,null=True,default=True)

    def __str__(self):
        return self.iemail

class Constable(models.Model):

    coemail = models.EmailField(unique=True)
    copassword = models.CharField(max_length=30)
    coname = models.CharField(max_length=50)
    cophone = models.CharField(max_length=15)
    coarea = models.CharField(max_length=50)

    def __str__(self):
        return self.coemail

class Manageinfo(models.Model):

    branchname = models.CharField(max_length=50)
    branchcode = models.CharField(max_length=10)
    cityname = models.CharField(max_length=50)
    branchphone = models.CharField(max_length=15)

    def __str__(self):
        return self.branchname