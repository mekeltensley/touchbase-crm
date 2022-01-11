from django.urls import path

# import view pages
from .views import ( 
        LeadCreateView, lead_delete, lead_update,
        LeadListView, LeadDetailView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/update/', lead_update, name="lead-update"),
    path('<int:pk>/delete/', lead_delete, name="lead-delete"),
    path('create/', LeadCreateView.as_view(), name="lead-create")
]
