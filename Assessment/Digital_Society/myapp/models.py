from django.db import models

# Create your models here.

class AddMember(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class AddNotice(models.Model):
    name=models.CharField(max_length=20)
    aboutnotice=models.TextField()
    date=models.DateTimeField()
    mobile=models.BigIntegerField()

class AddEvent(models.Model):
    eventname=models.CharField(max_length=20)
    eventdetail=models.CharField(max_length=100)
    datetime=models.DateTimeField()
    mobile=models.BigIntegerField()