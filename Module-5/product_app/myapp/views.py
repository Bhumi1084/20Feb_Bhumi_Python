from django.shortcuts import render,HttpResponse
#from product_app import settings
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def padmin(request):
    if request.method == 'POST':
        p_admin = pro_admin(request.POST)
        if p_admin.is_valid():
            p_admin.save()
            print("Product Added Successfully....!")
            #msg1 = "Product Add Successfully."
        else:
            print(p_admin.errors)
    return render(request,'padmin.html')

def product_manager(request):
    pnmData = product_master.objects.all()
    
    if request.method == 'POST':
        pro_manage = pmst(request.POST)
        if pro_manage.is_valid():
            pro_manage.save()
            print("Sub Product Added Successfully....!")
            #msg = "Sub Product Add Successfully."
        else:
            print(pro_manage.errors)  
    return render(request,'product_manager.html',{'pnmData' : pnmData})