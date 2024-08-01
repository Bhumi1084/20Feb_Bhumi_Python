from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def base(request):
    return render(request,'base.html')

def navbar(request):
    return render(request,'navbar.html')

# Society Member Backend code
def addmember(request):
    if request.method=='POST':
        memberdata = societymember(request.POST)
        if memberdata.is_valid():
            memberdata.save()
            print("Record inserted..!!")
            return redirect('showmember')
        else:
            print(memberdata.errors)
    return render(request,'addmember.html')

def showmember(request):
    memberdata = AddMember.objects.all()
    return render(request,'showmember.html',{'memberdata':memberdata})

def deletemember(request,id):
    mid=AddMember.objects.get(id=id)
    AddMember.delete(mid)
    return redirect('showmember')

def updatemember(request,id):
    mid = AddMember.objects.get(id=id)
    if request.method == 'POST':
        memberdata = societymember(request.POST,instance=mid)
        if memberdata.is_valid():
            memberdata.save()
            print("Record Updates...!!")
            return redirect('showmember')
        else:
            print(memberdata.errors)
    return render(request,'updatemember.html',{'mid':mid})


# Society Notice Backend code

def addnotice(request):
    if request.method=='POST':
        noticedata = notice(request.POST)
        if noticedata.is_valid():
            noticedata.save()
            print("Record inserted..!!")
            return redirect('shownotice')
        else:
            print(noticedata.errors)
    return render(request,'addnotices.html')

def shownotices(request):
    membernotice = AddNotice.objects.all()
    return render(request,'shownotices.html',{'membernotice':membernotice})

def deletnotice(request,id):
    nid=AddNotice.objects.get(id=id)
    AddNotice.delete(nid)
    return redirect('shownotice')

def updatenotice(request,id):
    nid = AddNotice.objects.get(id=id)
    if request.method == 'POST':
        membernotice = notice(request.POST,instance=nid)
        if membernotice.is_valid():
            membernotice.save()
            print("Record Updates...!!")
            return redirect('shownotice')
        else:
            print(membernotice.errors)
    return render(request,'updatenotice.html',{'nid':nid})

# Event Backend code

def addevent(request):
    if request.method=='POST':
        eventdata = event(request.POST)
        if eventdata.is_valid():
            eventdata.save()
            print("Record inserted..!!")
            return redirect('showevent')
        else:
            print(eventdata.errors)
    return render(request,'addevent.html')

def showevent(request):
    event = AddEvent.objects.all()
    return render(request,'showevent.html',{'event':event})

def deletevent(request,id):
    eid=AddEvent.objects.get(id=id)
    AddEvent.delete(eid)
    return redirect('showevent')

def updateevent(request,id):
    eid = AddEvent.objects.get(id=id)
    if request.method == 'POST':
        events = event(request.POST,instance=eid)
        if events.is_valid():
            events.save()
            print("Record Updates...!!")
            return redirect('showevent')
        else:
            print(events.errors)
    return render(request,'updateevent.html',{'eid':eid})

# Visitors Backend code

def addvisitor(request):
    if request.method=='POST':
        visitordata = visitors(request.POST)
        if visitordata.is_valid():
            visitordata.save()
            print("Record inserted..!!")
            return redirect('showvisitor')
        else:
            print(visitordata.errors)
    return render(request,'addvisitors.html')

def showvisitor(request):
    visitor = AddVisitors.objects.all()
    return render(request,'showvisitors.html',{'visitor':visitor})

def deletevisitor(request,id):
    vid=AddVisitors.objects.get(id=id)
    AddVisitors.delete(vid)
    return redirect('showvisitor')

def updatevisitor(request,id):
    vid = AddVisitors.objects.get(id=id)
    if request.method == 'POST':
        visitor = visitors(request.POST,instance=vid)
        if visitor.is_valid():
            visitor.save()
            print("Record Updates...!!")
            return redirect('showvisitor')
        else:
            print(visitor.errors)
    return render(request,'updatevisitors.html',{'vid':vid})

# Transaction Backend Code

def addtransaction(request):
    if request.method=='POST':
        transactiondata = transaction(request.POST)
        if transactiondata.is_valid():
            transactiondata.save()
            print("Record inserted..!!")
            return redirect('showtransaction')
        else:
            print(transactiondata.errors)
    return render(request,'addtransaction.html')

def showtransaction(request):
    transactions = AddTransaction.objects.all()
    return render(request,'showtransaction.html',{'transactions':transactions})

def deletetransaction(request,id):
    tid=AddTransaction.objects.get(id=id)
    AddTransaction.delete(tid)
    return redirect('showtransaction')