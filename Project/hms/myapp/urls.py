from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    # Login & Signup
    path('',views.base),
    path('signup/',views.signup),

    # Dashboard
    path('dashboard/',views.dashboard,name="dashboard"),

    # Doctors
    path('add_doctor/',views.add_doctor),
    path('all_doctors/',views.all_doctors,name="alldoctors"),
    path('doctor_details/<int:id>',views.doctor_details,name='doctor_detail'),
    path('update_doctor/<int:id>',views.update_doctor),
    path('delete_doctor/<int:id>',views.delete_doctor),
]