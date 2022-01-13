from typing_extensions import ParamSpecKwargs
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic 
from .models import Lead, Contact_Rep
from .forms import LeadForm, LeadModelForm



# Landing Page View
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, "landing.html")

# Lead List View 

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    # Returns a query set from the database
    # leads is  list of objects
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/lead_list.html", context)

#

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, "leads/lead_detail.html", context)

#

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
         return reverse("leads:lead-list") 


def lead_create(request):
    # when called, this will either create a new form and post form if set to POST
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

#

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
         return reverse("leads:lead-list") 

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,        
        "lead": lead
    }

    return render(request, "leads/lead_update.html", context)

#

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
         return reverse("leads:lead-list") 

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

