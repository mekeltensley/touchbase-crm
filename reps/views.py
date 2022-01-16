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
    
    def form_valid(self, form):
        rep = form.save(commit=False)
        rep.organization = self.request.user.userprofile
        rep.save()
        return super(ContactRepCreateView, self).form_valid(form)
    
class ContactRepDetailView(LoginRequiredMixin, generic.DetailView):
    
    template_name = "reps/rep_detail.html"
    context_object_name = "rep"
    
    
    def get_queryset(self):
        return Contact_Rep.objects.all()
    
    