# Has all forms in one file 
from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = {
            "email",
            "first_name",
            "last_name",
            "contact_rep",
        }
        

class LeadForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(max_length=10)