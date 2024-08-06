from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

# login pages
def base(request):
    if request.method=='POST':
        role=request.POST['role']
        unm=request.POST['username']
        pas=request.POST['password']

        user = users.objects.filter(role=role,username=unm,password=pas)
        if user:
            print("Login Successfully....!!!")
            return redirect('dashboard')
        else:
            print("Error...! Login Faile.")
    return render(request,'base.html')

# Signup page
def signup(request):
    if request.method=='POST':
        newuser = userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created...!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

# dashboard page
def dashboard(request):
    return render(request,'dashboard.html')

# Add Members
def members(request):
    if request.method=='POST':
        newmember = memberForm(request.POST)
        if newmember.is_valid():
            newmember.save()
            print("Record Inserted...!!")
            return redirect('showmembers')
        else:
            print(newmember.errors)
    return render(request,'members.html')

# Show Members
def showmembers(request):
    memberData = Members.objects.all()
    return render(request,'showmembers.html',{'memberData':memberData})

# Update Members
def updatemember(request, id):
    mid = Members.objects.get(id=id)
    if request.method=='POST':
        newData = memberForm(request.POST, instance=mid)
        if newData.is_valid():
            newData.save()
            print("Record Updated...!!")
            return redirect('showmembers')
        else:
            print(newData.errors)
    return render(request,'updatemember.html',{'mid':mid})

# Delete Members
def deletemember(request, id):
    mid = Members.objects.get(id=id)
    Members.delete(mid)
    return redirect('showmembers')

# Add Notices
def addnotices(request):
    if request.method=='POST':
        newnotice = noticesForm(request.POST)
        if newnotice.is_valid():
            newnotice.save()
            print("Record Inserted...!!")
            return redirect('shownotices')
        else:
            print(newnotice.errors)
    return render(request,'addnotices.html')

# Show Notices
def shownotices(request):
    notice = Notices.objects.all()
    return render(request,'shownotices.html',{'notice':notice})

# Update Notices
def updatenotices(request, id):
    nid = Notices.objects.get(id=id)
    if request.method=='POST':
        updatenotice=noticesForm(request.POST,instance=nid)
        if updatenotice.is_valid():
            updatenotice.save()
            print("Recored Updated...!!")
            return redirect('shownotices')
        else:
            print(updatenotice.errors)
    return render(request,'updatenotices.html',{'nid':nid})

# Delete Notices
def deletenotices(request, id):
    nid = Notices.objects.get(id=id)
    Notices.delete(nid)
    return redirect('shownotices')

# Add Transactions
def transactions(request):
    if request.method=='POST':
        newtransactions = transactionsForm(request.POST)
        if newtransactions.is_valid():
            newtransactions.save()
            print("Record Inserted...!!")
            return redirect('showtransactions')
        else:
            print(newtransactions.errors)
    return render(request,'transactions.html')

# Show Transactions
def showtransactions(request):
    alltransactions = Transactions.objects.all()
    return render(request,'showtransactions.html',{'alltransactions':alltransactions})

# Delete Transactions
def deletetransactions(request, id):
    tid = Transactions.objects.get(id=id)
    Transactions.delete(tid)
    return redirect('showtransactions')

# Update Transactions
def updatetransactions(request, id):
    tid = Transactions.objects.get(id=id)
    if request.method=='POST':
        updatetransaction=transactionsForm(request.POST,instance=tid)
        if updatetransaction.is_valid():
            updatetransaction.save()
            print("Recored Updated...!!")
            return redirect('showtransactions')
        else:
            print(updatetransaction.errors)
    return render(request,'updatetransactions.html',{'tid':tid})

# Add Watchman
def watchman(request):
    if request.method=='POST':
        newwatchman = watchmanForm(request.POST)
        if newwatchman.is_valid():
            newwatchman.save()
            print("Record Inserted...!!")
            return redirect('showwatchman')
        else:
            print(newwatchman.errors)
    return render(request,'watchmans.html')

# Show Watchman
def showwatchman(request):
    allwatchman = Watchmans.objects.all()
    return render(request,'showwatchmans.html',{'allwatchman':allwatchman})

# Delete Watchman
def deletewatchman(request, id):
    wid = Watchmans.objects.get(id=id)
    Watchmans.delete(wid)
    return redirect('showwatchman')

# Update Watchman
def updatewatchman(request, id):
    wid = Watchmans.objects.get(id=id)
    if request.method=='POST':
        updatewatchman=watchmanForm(request.POST,instance=wid)
        if updatewatchman.is_valid():
            updatewatchman.save()
            print("Recored Updated...!!")
            return redirect('showwatchman')
        else:
            print(updatewatchman.errors)
    return render(request,'updatewatchman.html',{'wid':wid})

# Add Visitors
def visitors(request):
    if request.method=='POST':
        newvisitor = VisitorsForm(request.POST)
        if newvisitor.is_valid():
            newvisitor.save()
            print("Record Inserted...!!")
            # return redirect('showvisitors')
        else:
            print(newvisitor.errors)
    return render(request,'visitors.html')

# Show Visitors
# def showvisitors(request):
#     allvisitors = Visitors.objects.all()
#     return render(request,'showvisitors.html',{'allvisitors':allvisitors})

# Delete Visitors
# def deletevisitors(request, id):
#     vid = Visitors.objects.get(id=id)
#     Visitors.delete(vid)
#     return redirect('showvisitors')

# Update Visitors
# def updatevisitors(request, id):
#     vid = Visitors.objects.get(id=id)
#     if request.method=='POST':
#         updatevisitors=VisitorsForm(request.POST,instance=vid)
#         if updatevisitors.is_valid():
#             updatevisitors.save()
#             print("Recored Updated...!!")
#             return redirect('showvisitors')
#         else:
#             print(updatevisitors.errors)
#     return render(request,'updatevisitors.html',{'vid':vid})