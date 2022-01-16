from django.urls import path
from .views import ContactRepDetailView, ContactRepListView, ContactRepCreateView

app_name = 'reps'

urlpatterns = [
    path('', ContactRepListView.as_view(), name='rep-list'), 
    path('<int:pk>/', ContactRepDetailView.as_view(), name="rep-detail"),
    # path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),
    # path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('create/', ContactRepCreateView.as_view(), name='rep-create'), 
]