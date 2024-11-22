from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    # Login & Signup, Logout
    path('',views.base),
    path('signup/',views.signup),
    path('userlogout/',views.userlogout),

    # Dashboard
    path('dashboard/',views.dashboard,name="dashboard"),

    # NavigationBar
    path('navbar/',views.navbar),

    # Doctors
    path('add_doctor/',views.add_doctor),
    path('all_doctors/',views.all_doctors,name="alldoctors"),
    path('doctor_details/<int:id>',views.doctor_details,name='doctor_detail'),
    path('update_doctor/<int:id>',views.update_doctor),
    path('delete_doctor/<int:id>',views.delete_doctor),

    # Patient
    path('add_patient/',views.add_patient), 
    path('all_patient/',views.all_patient,name="allpatient"),
    path('delete_patient/<int:id>',views.delete_patient),
    path('update_patient/<int:id>',views.update_patient),
    path('patient_details/<int:id>',views.patient_details),

    # Appointment
    path('add_appointment/',views.add_appointment),
]