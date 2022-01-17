from django.urls import path
from .views import (
    ContactRepDeleteView, ContactRepDetailView, ContactRepListView, 
    ContactRepCreateView, ContactRepUpdateView
)

app_name = 'reps'

urlpatterns = [
    path('', ContactRepListView.as_view(), name='rep-list'), 
    path('<int:pk>/', ContactRepDetailView.as_view(), name='rep-detail'),
    path('<int:pk>/update/', ContactRepUpdateView.as_view(), name='rep-update'),
    path('<int:pk>/delete/', ContactRepDeleteView.as_view(), name='rep-delete'),
    path('create/', ContactRepCreateView.as_view(), name='rep-create'), 
]