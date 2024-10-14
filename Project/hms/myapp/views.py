from django.shortcuts import render, redirect, get_list_or_404
from .forms import *

# Create your views here.

# Dashboard
def dashboard(request):
    return render(request,'dashboard.html')

# Login
def base(request):
    if request.method=='POST':
        role=request.POST['role']
        unm=request.POST['username']
        pas=request.POST['password']

        user = userdata.objects.filter(role=role,username=unm,password=pas)
        if user:
            print("Login Successfully....!!!")
            return redirect('dashboard')
        else:
            print("Error...! Login Faile.")    
    return render(request,'base.html')

# SignUp
def signup(request):
    if request.method=='POST':
        newuser = userdataForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created...!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

# Add Doctor
def add_doctor(request):
    msg=""
    if request.method=='POST':
        newdoctor = addDocotrForm(request.POST)
        if newdoctor.is_valid():
            newdoctor.save()
            print("Record Inserted...!!")
            msg="Successfully Done! Please Check in doctors list"
            return redirect('alldoctors')
        else:
            print(newdoctor.errors)
            msg="Holy guacamole! You should check in on some of those fields below."
    return render(request,'add_doctor.html',{'msg':msg})

# Update Doctor
def update_doctor(request, id):
    msg=""
    docid = addDoctor.objects.get(id=id)
    if request.method=='POST':
        newdoc = addDocotrForm(request.POST, instance=docid)
        if newdoc.is_valid():
            newdoc.save()
            print("Recored is updated..!!")
            msg="Successfully Done! Please Check in doctors list"
            return redirect('alldoctors')
        else:
            print(newdoc.errors)
            msg="Holy guacamole! You should check in on some of those fields below."
    return render(request,'update_doctor.html',{'docid':docid, 'msg':msg})

# All Doctors List
def all_doctors(request):
    showdoctor = addDoctor.objects.all()
    return render(request,'all_doctors.html',{'showdoctor':showdoctor})

# Doctor Details
def doctor_details(request,id):
    doctor = addDoctor.objects.get(id=id)
    return render(request,'doctor_details.html', {
        'doctor': doctor,
    })

# Delete Doctor
def delete_doctor(request,id):
    docid = addDoctor.objects.get(id=id)
    addDoctor.delete(docid)
    return redirect('alldoctors')