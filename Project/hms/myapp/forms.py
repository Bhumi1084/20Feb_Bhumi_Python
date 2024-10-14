from django import forms
from .models import *

# SignUp & Login
class userdataForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields='__all__'

# Add Doctor
class addDocotrForm(forms.ModelForm):
    class Meta:
        model=addDoctor
        fields='__all__'