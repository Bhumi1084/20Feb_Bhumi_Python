from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [    
    path('',views.base),
    path('navbar/', views.navbar),
    path('addmember/',views.addmember),
    path('showmember/',views.showmember, name='showmember'),
    path('deletemember/<int:id>',views.deletemember),
    path('updatemember/<int:id>',views.updatemember),
    path('addnotice/',views.addnotice),
    path('shownotices/',views.shownotices, name='shownotice'),
    path('deletnotice/<int:id>',views.deletnotice),
    path('updatenotice/<int:id>',views.updatenotice),
]