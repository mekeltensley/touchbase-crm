from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Contact_Rep


class ContactRepListView(LoginRequiredMixin, generic.ListView):
    template_name = "reps/rep_list.html"
    
    def get_queryset(self):
        return Contact_Rep.objects.all()