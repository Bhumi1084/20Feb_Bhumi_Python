from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import requests

# Create your views here.

def index(request):
    url="http://127.0.0.1:8000/getall/"
    req=requests.get(url)
    blogdata=req.json()
    return render(request,'index.html',{'blogdata':blogdata})

@api_view(['GET'])
def getall(request):
    blogdata=blogmodel.objects.all()
    serial=blogSerial(blogdata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getid(request,id):
    try:
        blogid=blogmodel.objects.get(id=id)
    except blogmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=blogSerial(blogid)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        blogid=blogmodel.objects.get(id=id)
    except blogmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=blogSerial(blogid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        blogmodel.delete(blogid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=blogSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        blogid=blogmodel.objects.get(id=id)
    except blogmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=blogSerial(blogid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=blogSerial(data=request.data,instance=blogid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)