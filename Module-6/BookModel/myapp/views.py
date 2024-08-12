from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

def index(request):
    # bookdata=bookinfo.objects.all()
    url="http://127.0.0.1:8000/getall/"
    req=requests.get(url)
    bookdata=req.json()
    return render(request,'index.html',{'bookdata':bookdata})

# get all data
@api_view(['GET'])
def getall(request):
    bookdata=bookinfo.objects.all()
    serial=bookSerial(bookdata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)

# get any one data
@api_view(['GET'])  
def getbookid(request,id):
    try:
        bookid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookSerial(bookid)
    return Response(data=serial.data,status=status.HTTP_200_OK)

# delet data
@api_view(['GET','DELETE'])
def deletebookid(request,id):
    try:
        bookid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookSerial(bookid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        bookinfo.delete(bookid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
# insert data
@api_view(['POST'])
def savebookdata(request):
    if request.method=='POST':
        print(request.data)
        serial=bookSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# update data
@api_view(['GET','PUT'])
def updatebookdata(request,id):
    try:
        bookid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookSerial(bookid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=bookSerial(data=request.data,instance=bookid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)