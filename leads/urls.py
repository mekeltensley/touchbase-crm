from django.urls import path

# import view pages
from .views import ( 
        AssignContactRepView, lead_delete, lead_update, lead_list, lead_create, lead_detail,
        LeadCreateView, LeadUpdateView, LeadListView, LeadDetailView, LeadDeleteView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/assign-contact-rep/', AssignContactRepView.as_view(), name="assign-contact-rep"),
]
