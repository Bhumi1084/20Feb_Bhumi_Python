from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('product_manager/',views.product_manager),   
    path('padmin/',views.padmin),
]