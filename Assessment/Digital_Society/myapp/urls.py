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
    path('addevent/',views.addevent),
    path('showevent/',views.showevent, name='showevent'),
    path('deletevent/<int:id>',views.deletevent),
    path('updateevent/<int:id>',views.updateevent),
    path('addvisitor/',views.addvisitor),
    path('showvisitor/',views.showvisitor, name='showvisitor'),
    path('deletevisitor/<int:id>',views.deletevisitor),
    path('updatevisitor/<int:id>',views.updatevisitor),
    path('addtransaction/',views.addtransaction),
    path('showtransaction/',views.showtransaction, name='showtransaction'),
    path('deletetransaction/<int:id>',views.deletetransaction),
]