from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

# Create your views here.
def Dashboard(request):
    user = request.session.get('user')
    return render(request,'Dashboard.html',{'user':user})

def SignUp(request):
    return render(request,'SignUp.html')

def Login(request):
    return render(request,'Login.html')

def MyProfile(request):
    return render(request,'MyProfile.html')

def SocietyMembers(request):
    return render(request,'SocietyMembers.html')

def ShowMember(request):
    return render(request,'ShowMember.html')

def RemoveMember(request):
    return render(request,'RemoveMember.html')

def SocietyWatchmen(request):
    return render(request,'SocietyWatchmen.html')

def ShowWatchmenDetails(request):
    return render(request,'ShowWatchmenDetails.html')

def RemoveWatchmen(request):
    return render(request,'RemoveWatchmen.html')

def Notice(request):
    return render(request,'Notice.html')

def ShowNotice(request):
    return render(request,'ShowNotice.html')

def RemoveNotice(request):
    return render(request,'RemoveNotice.html')

def Event(request):
    return render(request,'Event.html')

def ShowEvent(request):
    return render(request,'ShowEvent.html')

def RemoveEvent(request):
    return render(request,'RemoveEvent.html')