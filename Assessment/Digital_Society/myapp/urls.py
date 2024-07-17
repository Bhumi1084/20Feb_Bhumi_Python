from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Dashboard),
    path('SignUp/',views.SignUp),
    path('Login/',views.Login),
    path('MyProfile/',views.MyProfile),
    path('SocietyMembers/',views.SocietyMembers),
    path('ShowMember/',views.ShowMember),
    path('RemoveMember/',views.RemoveMember),
    path('SocietyWatchmen/',views.SocietyWatchmen),
    path('ShowWatchmenDetails/',views.ShowWatchmenDetails),
    path('RemoveWatchmen/',views.RemoveWatchmen),
    path('Notice/',views.Notice),
    path('ShowNotice/',views.ShowNotice),
    path('RemoveNotice/',views.RemoveNotice),
    path('Event/',views.Event),
    path('ShowEvent/',views.ShowEvent),
    path('RemoveEvent/',views.RemoveEvent),
]