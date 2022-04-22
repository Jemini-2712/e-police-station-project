from distutils.log import info
import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 

# Create your views here.

def home(request):
    return render(request,'home.html')
    
def commissioner_login(request):
    if request.method == 'POST':
        try:
            uid = Commissioner.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session ['email'] = request.POST['email']
                return render(request,'home.html')
            return render(request,'commissioner-login.html',{'msg':'password is incorrect'})    
        except:
            return render(request,'commissioner-login.html',{'msg':'Account does not exist'})

    return render(request,'commissioner-login.html')

def add_inspector(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Inspector.objects.create(
            iemail = request.POST['iemail'],
            ipassowrd = request.POST['ipassword'],
            iname = request.POST['iname'],
            iphone = request.POST['iphone'],
            iarea = request.POST['iarea'],
        )
    return render(request,'add-inspector.html',{'uid':uid})

def inspector_update(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    ins = Inspector.objects.get(id=pk)
    if request.method == 'POST':
        ins.iname = request.POST['iname']
        ins.iphone = request.POST['iphone']
        ins.iarea = request.POST['iarea']
        ins.save()
        return redirect('view-inspectors')

    else:
        return render(request,'inspector-update.html',{'uid':uid,'ins':ins})
    

def delete_inspector(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    ins = Inspector.objects.get(id=pk)
    ins.delete()
    return redirect('view-inspectors')

def add_constable(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Constable.objects.create(
            coemail = request.POST['coemail'],
            copassword = request.POST['copassword'],
            coname = request.POST['coname'],
            cophone = request.POST['cophone'],
            coarea = request.POST['coarea'],
        )
    return render(request,'add-constable.html',{'uid':uid})

def constable_update(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    con = Constable.objects.get(id=pk)
    if request.method == 'POST':
        con.coname = request.POST['coname']
        con.cophone = request.POST['cophone']
        con.coarea = request.POST['coarea']
        con.save()
        return redirect('view-constables')

    else:
        return render(request,'constable-update.html',{'uid':uid,'con':con})

def delete_constable(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    con = Constable.objects.get(id=pk)
    con.delete()
    return redirect('view-constables')

def view_inspectors(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    inspectors = Inspector.objects.all()
    return render(request,'view-inspectors.html',{'uid':uid,'inspectors':inspectors})

def view_constables(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    constables = Constable.objects.all()
    return render(request,'view-constables.html',{'uid':uid,'constables':constables})

def addinfo(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Manageinfo.objects.create(
            branchname = request.POST['branchname'],
            branchcode = request.POST['branchcode'],
            cityname = request.POST['cityname'],
            branchphone = request.POST['branchphone'],
        )
        return redirect('manageinfo')
    return render(request,'addinfo.html',{'uid':uid})

def manageinfo(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    info = Manageinfo.objects.all()
    return render(request,'manageinfo.html',{'info':info,'uid':uid})

def manageinfo_update(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    info = Manageinfo.objects.get(id=pk)
    if request.method == 'POST':
        info.branchname = request.POST['branchname']
        info.branchcode = request.POST['branchcode']
        info.cityname = request.POST['cityname']
        info.branchphone = request.POST['branchphone']
        info.save()
        return redirect('manageinfo')

    else:
        return render(request,'manageinfo-update.html',{'uid':uid,'info':info})

def delete_info(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    info = Manageinfo.objects.get(id=pk)
    info.delete()
    return redirect('manageinfo')


def log_out(request):
    try:
        request.session['email']
        del request.session['email']
        return render(request,'commissioner-login.html')
    except: 
        return render(request,'commissioner-login.html')

def firs(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    firs = Fir.objects.all()
    return render(request,'firs.html',{'uid':uid,'firs':firs})

def completed_action(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    firs = Fir.objects.get(id=pk)
    firs.status = True
    firs.solved_by = uid
    firs.save()
    return redirect('firs')

def action_completed(request,pk):
    uid = Commissioner.objects.get(email=request.session['email'])
    complaints = Complaint.objects.get(id=pk)
    complaints.cstatus = True
    complaints.solvedby = uid
    complaints.save()
    return redirect('complaints')

def complaints(request):
    uid = Commissioner.objects.get(email=request.session['email'])
    complaints = Complaint.objects.all()
    return render(request,'complaints.html',{'uid':uid,'complaints':complaints})

