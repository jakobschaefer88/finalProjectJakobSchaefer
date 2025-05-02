from django.urls import path
from . import views

app_name = "groups"

urlpatterns = [
    path('', views.group_dashboard, name='group_dashboard'),
    # Add other group-related URLs here
]