from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_dashboard, name='group_dashboard'),
]