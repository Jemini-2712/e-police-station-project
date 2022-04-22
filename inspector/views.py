from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 

# Create your views here.

def first(request):
    return render(request,'first.html')

def inspector_login(request):
    if request.method == 'POST':
        try:
            uid = Inspector.objects.get(iemail=request.POST['iemail'])
            if request.POST['ipassowrd'] == uid.ipassowrd:
                request.session ['iemail'] = request.POST['iemail']
                return render(request,'first.html')
            return render(request,'inspector-login.html',{'msg':'password is incorrect'})    
        except:
            return render(request,'inspector-login.html',{'msg':'Account does not exist'})

    return render(request,'inspector-login.html')

def show_fir(request):
    uid = Inspector.objects.get(iemail=request.session['iemail'])
    showfirs = Fir.objects.all()
    return render(request,'show-fir.html',{'uid':uid,'showfirs':showfirs})

def show_complaints(request):
    uid = Inspector.objects.get(iemail=request.session['iemail'])
    showcomplaints = Complaint.objects.all()
    return render(request,'show-complaints.html',{'uid':uid,'showcomplaints':showcomplaints})

# def pending(request,pk):
#     uid = Inspector.objects.get(email=request.session['email'])
#     complaints = Complaint.objects.get(id=pk)
#     complaints.cstatus = False
#     complaints.save()
#     return redirect('complaints')

# def completed(request,pk):
#     uid = Inspector.objects.get(iemail=request.session['iemail'])
#     complaints = Complaint.objects.get(id=pk)
#     complaints.cstatus = True
#     complaints.save()
#     complaints.solvedby = uid
#     return redirect('complaints')

def sign_out(request):
    try:
        request.session['iemail']
        del request.session['iemail']
        return render(request,'inspector-login.html')
    except: 
        return render(request,'inspector-login.html')
