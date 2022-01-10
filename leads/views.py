from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Contact_Rep
from .forms import LeadForm


# function based views 

#renders list of leads

def lead_list(request):
    # Returns a query set from the database 
    # leads is  list of objects
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

#displays each lead by primary key 

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
 
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    # when called, this will either create a new form and post form if set to POST
    form = LeadForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            contact_rep = Contact_Rep.objects.first()
            Lead.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                contact_rep=contact_rep
            )
            print("Lead has been created")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
