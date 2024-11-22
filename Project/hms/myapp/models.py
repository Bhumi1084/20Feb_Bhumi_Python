from django.db import models

# Create your models here.

# Login & SignUp
class userdata(models.Model):
    role=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    cpass=models.CharField(max_length=30)

# Add Doctor
class addDoctor(models.Model):
    doctor_name=models.CharField(max_length=30)
    dob=models.DateField()
    specialization=models.CharField(max_length=50)
    experience=models.CharField(max_length=30)
    age=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=30)
    doctor_details=models.CharField(max_length=100)
    address=models.CharField(max_length=100)    

# Add Patient
class addPatients(models.Model):
    patient_name=models.CharField(max_length=30)
    dob=models.DateField()
    age=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=150)
    last_visit=models.DateField()