from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Contact_Rep
from .forms import LeadForm, LeadModelForm


# function based views

# renders list of leads


def lead_list(request):
    # Returns a query set from the database
    # leads is  list of objects
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/lead_list.html", context)


# displays each lead by primary key


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, "leads/lead_detail.html", context)


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

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             phone_number = form.cleaned_data['phone_number']
#             # Updates these field only
#             lead.email = email
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.phone_number = phone_number
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)
