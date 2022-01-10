from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# function based views 

def lead_list(request):
    # Returns a query set from the database 
    # leads is  list of objects
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
 
    return render(request, "leads/lead_detail.html", context)
