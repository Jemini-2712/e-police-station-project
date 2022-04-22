from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from policestation.models import Complaint, Fir, Manageinfo
from .models import *
from django.conf import settings
from random import randrange,choices
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request,'index.html')



def register(request):
    if request.method == 'POST':
        try:
         User.objects.get(email=request.POST['email'])
         msg = 'email already exist!!!' 
         return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['pass'] == request.POST['cpass']:
                otp = randrange(1000,9999)
                subject = 'OTP verification'
                message = f'Your otp is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                temp = {
                   'uname' : request.POST['uname'],
                    'email' : request.POST['email'],
                    'city' : request.POST['city'],
                    'password' : request.POST['pass'],
                    'state' : request.POST['state'],

                }

                return render(request,'otp.html',{'msg':'OTP sent on your email','otp':otp})
        return render(request,'register.html',{'msg':'Both are not same!!!'})
    return render(request,'register.html')
      

def citizen_login(request):
    if request.method == 'POST':
        # try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['pass'] == uid.password:
                request.session ['email'] = request.POST['email']
                return render(request,'citizen-dashboard.html')
            return render(request,'citizen-login.html',{'msg':'password is incorrect'})    
        # except:
        #     return render(request,'citizen-login.html',{'msg':'Account does not exist'})

    return render(request,'citizen-login.html')

def otp(request):
    if request.POST['uotp'] == request.POST['otp']:
        global temp
        User.objects.create(
            uname = temp['uname'],
            email = temp['email'],
            state = temp['state'],
            city = temp['city'],
            password = temp['password'],
        )
        del temp
        return render(request,'citizen-login.html',{'msg':'Account created!!'})
        
    return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})

def f_password(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])  
            s = 'dnfckqwertwshfbwdkfihwehdbkjedhbcdg1234567890'
            password = ''.join(choices(s,k=8))
            subject = 'Password Has been Reset'
            message = f'Your New Password is {password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return render(request,'citizen-login.html',{'msg':'New Password sent on your email'})
        except:
            return render(request,'f-password.html',{'msg':'Account does not exist'})
    return render(request,'f-password.html')

def profile(request):
    return render(request,'profile.html')
    
def change_password(request):
    if request.method == 'POST':
        uid = User.objects.get(email=request.session['email'])
        if request.POST['opass'] == uid.password :
            if request.POST['npass'] == request.POST['cpass'] :
                 uid.password=request.POST['cpass']
                 uid.save()
                 return render(request,'change-password.html',{'msg':'Password updated successfully.'})
            return render(request,'change-password.html',{'msg':'New password and confirm password does not match','uid' : uid})
        return render(request,'change-password.html',{'msg':'old password does not match'})   
    return render(request,'change-password.html')         
          


def addfir(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Fir.objects.create(
            pname = uid,
            cname = request.POST['cname'],
            phone = request.POST['phone'],
            #date = request.POST['date'],
            address = request.POST['address'],
            fir = request.POST['fir'],
            pic = request.POST['pic'],        
        )
    return render(request,'addfir.html')


def addcomplaint(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Complaint.objects.create(
            cpname = uid,
            ccname = request.POST['ccname'],
            cphone = request.POST['cphone'],
            #date = request.POST['date'],
            caddress = request.POST['caddress'],
            complaint = request.POST['complaint'],
            picture = request.POST['picture']

        )
    return render(request,'addcomplaint.html')

def feedback(request):
    if request.method == 'POST':
         Feedback.objects.create(
            fpname = request.POST['fpname'],
            fphone = request.POST['fphone'],
            feedback = request.POST['feedback']
        )
    return render(request,'feedback.html')

def viewfir(request):
    uid = User.objects.get(email=request.session['email'])
    fir = Fir.objects.filter(pname=uid)
    
    return render(request,'viewfir.html',{'fir':fir})

def viewcomplaint(request):
    uid = User.objects.get(email=request.session['email'])
    complaint = Complaint.objects.filter(cpname=uid)
    return render(request,'viewcomplaint.html',{'complaint':complaint})

def logout(request):
    try:
        request.session['email']
        del request.session['email']
        return render(request,'citizen-login.html')
    except: 
        return render(request,'citizen-login.html')


def citizen_dashboard(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'citizen-dashboard.html',{'uid':uid})
    except:
        return render(request,'citizen-login.html',{'msg':'session has expired'})

def edit_profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.uname = request.POST['uname']
        uid.city = request.POST['city']
        uid.state = request.POST['state']
        uid.save()
        return render(request,'edit-profile.html',{'uid':uid,'msg':'Profile has been updated successfully!!!'})
    return render(request,'edit-profile.html',{'uid':uid})

def policestations(request):
    uid = User.objects.get(email=request.session['email'])
    pinfo = Manageinfo.objects.all()
    return render(request,'policestations.html',{'uid':uid,'pinfo':pinfo})