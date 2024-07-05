from django import forms
from .models import *

class pro_admin(forms.ModelForm):
     class Meta:
        model = product_master
        fields = '__all__'

class pmst(forms.ModelForm):
     class Meta:
        model = sub_product
        fields = '__all__'        