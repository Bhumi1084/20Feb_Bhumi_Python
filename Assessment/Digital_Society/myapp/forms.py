from django import forms
from .models import *

class societymember(forms.ModelForm):
    class Meta:
        model=AddMember
        fields='__all__'

class notice(forms.ModelForm):
    class Meta:
        model=AddNotice
        fields='__all__'

class event(forms.ModelForm):
    class Meta:
        model=AddEvent
        fields='__all__'