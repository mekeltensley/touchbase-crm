from audioop import reverse
from re import template
from django.views import generic
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Contact_Rep
from .forms import ContactRepModelForm


class ContactRepListView(LoginRequiredMixin, generic.ListView):
    template_name = "reps/rep_list.html"
    
    def get_queryset(self):
        return Contact_Rep.objects.all()
    
class ContactRepCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "reps/rep_create.html"
    form_class = ContactRepModelForm
    
    def get_success_url(self):
        return reverse("reps:rep-list")