from django import forms
from leads.models import Contact_Rep

class ContactRepModelForm(forms.ModelForm):
    class Meta:
        model = Contact_Rep
        fields = ('user',)