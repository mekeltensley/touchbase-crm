# Has all forms in one file 
from django import forms

class LeadForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(max_length=10)