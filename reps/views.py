import random
from django.http import request
from django.views import generic
from django.shortcuts import reverse
from platformdirs import user_cache_dir
from leads.models import Contact_Rep
from .forms import ContactRepModelForm
from .mixins import OrganizerAndLoginRequiredMixin


class ContactRepListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "reps/rep_list.html"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Contact_Rep.objects.filter(organization=organization)
    
class ContactRepCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "reps/rep_create.html"
    form_class = ContactRepModelForm
    
    def get_success_url(self):
        return reverse("reps:rep-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_contact_rep = True
        user.is_admin = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Contact_Rep.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        return super(ContactRepCreateView, self).form_valid(form)
    
class ContactRepDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    
    template_name = "reps/rep_detail.html"
    context_object_name = "rep"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Contact_Rep.objects.filter(organization=organization)
    
class ContactRepUpdateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "reps/rep_update.html"
    form_class = ContactRepModelForm
    
    def get_success_url(self):
        return reverse("reps:rep-list")
    
class ContactRepDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    
    template_name = "reps/rep_delete.html"
    context_object_name = "rep"

    def get_success_url(self):
        return reverse("reps:rep-list")
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Contact_Rep.objects.filter(organization=organization)