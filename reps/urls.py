from django.urls import path
from .views import ContactRepListView

app_name = 'reps'

urlpatterns = [
    path('', ContactRepListView.as_view(), name='reps') 
]