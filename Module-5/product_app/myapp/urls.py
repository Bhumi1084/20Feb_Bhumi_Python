from django.urls import path,include
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('product_manager_add/',views.product_manager_add),   
    path('padmin_add/',views.padmin_add),
    path('padmin/',views.padmin),
    path('padmin_show/',views.padmin_show,name='showdata'),
    path('padmin_update/<int:id>',views.padmin_update),
    path('padmin_delete/<int:id>',views.padmin_delete),
]