from django.shortcuts import render,get_object_or_404, redirect
#from product_app import settings
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def padmin_add(request):
    if request.method == 'POST':
        p_admin = pro_admin(request.POST)
        if p_admin.is_valid():
            p_admin.save()
            print("Product Added Successfully....!")
            #msg1 = "Product Add Successfully."
        else:
            print(p_admin.errors)
    return render(request,'padmin_add.html')

def product_manager_add(request):
    pnmData = product_master.objects.all()
    
    if request.method == 'POST':
        pro_manage = pmst(request.POST)
        if pro_manage.is_valid():
            pro_manage.save()
            print("Sub Product Added Successfully....!")
            #msg = "Sub Product Add Successfully."
        else:
            print(pro_manage.errors)  
    return render(request,'product_manager_add.html',{'pnmData' : pnmData})

def padmin(request):
    return render(request,'padmin.html')

def product_manager(request):
    return render(request,'product_manager.html')

def padmin_update(request,id):
    pid = product_master.objects.get(id=id)
    if request.method=='POST':
        padmin_data = pro_admin(request.POST,instance=pid)
        if padmin_data.is_valid():
            padmin_data.save()
            print("Recored Updated...!")
            return redirect('showdata')
        else:
            print(padmin_data.errors)
    return render(request,'padmin_update.html',{'pid':pid})

def product_manager_update(request,id):
    pmid = get_object_or_404(sub_product, id=id)
    if request.method == 'POST':
        pmanager_data = pmst(request.POST, request.FILES, instance=pmid)
        if pmanager_data.is_valid():
            pmanager_data.save()
            print("Record Updated...!!")
            return redirect('pmanager_show')
        else:
            print(pmanager_data.errors)
    else:
        pmanager_data = pmst(instance=pmid)
    return render(request,'product_manager_update.html',{'form': pmanager_data,'pmid':pmid})

def padmin_show(request):
    padmin_data = product_master.objects.all()
    return render(request,'padmin_show.html',{'padmin_data':padmin_data})

def product_manager_show(request):
    pmanager_data = sub_product.objects.all()
    return render(request,'product_manager_show.html',{'pmanager_data':pmanager_data})

def padmin_delete(request,id):
    pid = product_master.objects.get(id=id)
    product_master.delete(pid)
    return redirect('showdata')

def product_manager_delete(request,id):
    pmid = sub_product.objects.get(id=id)
    sub_product.delete(pmid)
    return redirect('pmanager_show')