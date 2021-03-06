from django import forms
from .models import LEAD_STATUS, SOURCE_CHOICES, Lead, User, Contact_Rep
from django.contrib.auth.forms import UserCreationForm, UsernameField


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'last_contacted',
            'lead_status',
            'source_of_lead',
            'contact_rep',
        ]
        

class LeadForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(max_length=10)
    last_contacted = forms.CharField()
    lead_status = forms.Select(choices=LEAD_STATUS)
    source_of_lead = forms.Select(choices=SOURCE_CHOICES)
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = {"username", }
        field_classes = {'username': UsernameField}
        
class AssignContactRepForm(forms.Form):
    representatives = forms.ModelChoiceField(queryset=Contact_Rep.objects.none())
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        representatives = Contact_Rep.objects.filter(organization=request.user.userprofile)
        super(AssignContactRepForm, self).__init__(*args, **kwargs)
        self.fields["representatives"].queryset = representatives