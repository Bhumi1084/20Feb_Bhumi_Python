from django.db import models

# Create your models here.

class users(models.Model):
    role=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Members(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class Notices(models.Model):
    sendername=models.CharField(max_length=20)
    receivername=models.CharField(max_length=20)
    details=models.TextField()
    mobile=models.BigIntegerField()
    datetime=models.DateTimeField()

class Transactions(models.Model):
    amountsendernm=models.CharField(max_length=20)
    amountreceivernm=models.CharField(max_length=20)
    amount=models.BigIntegerField()
    datetime=models.DateTimeField()

class Watchmans(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    joiningDate=models.DateField()
    dayshift=models.CharField(max_length=20)

class Visitors(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=20)
    datetime=models.DateTimeField()

class Event(models.Model):
    eventname=models.CharField(max_length=20)
    email=models.EmailField()
    eventdate=models.DateTimeField()
    description=models.TextField()
    mobile=models.BigIntegerField()