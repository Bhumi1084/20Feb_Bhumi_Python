from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # Handle successful login
        else:
            messages.error(request,'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Handle logout
    return redirect('login')

def Signup(request):
    return render(request,'Signup.html')

def Dashboard(request):
    return render(request,'Dashboard.html')

def event(request):
    return render(request,'event.html')

def myprofile(request):
    return render(request,'myprofile.html')

def societymember(request):
    return render(request,'societymember.html')

def societywatchmen(request):
    return render(request,'societywatchmen.html')

def notice(request):
    return render(request,'notice.html')