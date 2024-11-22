from django.shortcuts import render, redirect, get_list_or_404
from .forms import *
from django.contrib.auth import logout

# Create your views here.

# Dashboard
def dashboard(request):
    return render(request,'dashboard.html')

# NavigationBar
def navbar(request):
    return render(request,'navbar.html')

# Logout
def userlogout(request):
    logout(request)
    return redirect('/')

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

# Add Patient
def add_patient(request):
    msg=""
    if request.method=='POST':
        newpatient = addPatientForm(request.POST)
        if newpatient.is_valid():
            newpatient.save()
            print("Record Inserted....!!")
            msg="Successfully Done! Please add payment now"
            return redirect('allpatient')
        else:
            print(newpatient.errors)
            msg="Holy guacamole! You should check in on some of those fields below."
    return render(request,'add_patient.html',{'msg':msg})

# Add Appointment
def add_appointment(request):
    return render(request,'add_appointment.html')



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

# Update Patient
def update_patient(request, id):
    msg=""
    patientid = addPatients.objects.get(id=id)
    if request.method=='POST':
        newpatient = addPatientForm(request.POST, instance=patientid)
        if newpatient.is_valid():
            newpatient.save()
            print("Recored is updated..!!")
            msg="Successfully Done! Please add payment now"
            return redirect('allpatient')
        else:
            print(newpatient.errors)
            msg="Holy guacamole! You should check in on some of those fields below."
    return render(request,'update_patient.html',{'patientid':patientid, 'msg':msg})



# All Doctors List
def all_doctors(request):
    showdoctor = addDoctor.objects.all()
    return render(request,'all_doctors.html',{'showdoctor':showdoctor})

# All Patient List
def all_patient(request):
    showpatient = addPatients.objects.all()
    return render(request,'all_patient.html',{'showpatient':showpatient})



# Doctor Details
def doctor_details(request,id):
    doctor = addDoctor.objects.get(id=id)
    return render(request,'doctor_details.html', {
        'doctor': doctor,
    })

# Patient Details
def patient_details(request, id):
    patient = addPatients.objects.get(id=id)
    return render(request,'patient_details.html', {
        'patient': patient,
    }) 



# Delete Doctor
def delete_doctor(request,id):
    docid = addDoctor.objects.get(id=id)
    addDoctor.delete(docid)
    return redirect('alldoctors')

# Delete Patient
def delete_patient(request,id):
    patientid = addPatients.objects.get(id=id)
    addPatients.delete(patientid)
    return redirect('allpatient')