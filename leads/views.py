from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic 
from reps.mixins import OrganizerAndLoginRequiredMixin
from .models import Lead, Contact_Rep
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm, AssignContactRepForm



class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
         return reverse("login")
    
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, "landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            queryset = Lead.objects.filter(organization=user.userprofile, 
            contact_rep__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.contact_rep.organization, 
            contact_rep__isnull=False)
            queryset = queryset.filter(contact_rep__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_admin:
            queryset = Lead.objects.filter(
                organization=user.userprofile, 
                contact_rep__isnull=True)
        context.update({
            "unassigned_leads": queryset
        })
        return context

def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/lead_list.html", context)

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, "leads/lead_detail.html", context)

class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
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

class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    
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

class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    
    def get_success_url(self):
         return reverse("leads:lead-list") 
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


class AssignContactRepView(OrganizerAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_rep.html"
    form_class = AssignContactRepForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignContactRepView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        
        return kwargs
    
    def get_success_url(self):
         return reverse("leads:lead-list") 
     
    def form_valid(self, form):
        contact_rep = form.cleaned_data["representatives"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.contact_rep = contact_rep
        lead.save()
        return super(AssignContactRepView, self).form_valid(form)