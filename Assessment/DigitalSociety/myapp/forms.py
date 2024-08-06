from django import forms
from .models import *

# SignUp & Login
class userForm(forms.ModelForm):
    class Meta:
        model=users
        fields='__all__'

# Society Member
class memberForm(forms.ModelForm):
    class Meta:
        model=Members
        fields='__all__'

# Notices
class noticesForm(forms.ModelForm):
    class Meta:
        model=Notices
        fields='__all__'

# Transactions
class transactionsForm(forms.ModelForm):
    class Meta:
        model=Transactions
        fields='__all__'

# Watchman
class watchmanForm(forms.ModelForm):
    class Meta:
        model=Watchmans
        fields='__all__'

# Visitors
class VisitorsForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields='__all__'

# Event
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'