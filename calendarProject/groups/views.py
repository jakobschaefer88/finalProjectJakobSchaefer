# groups/views.py
from django.shortcuts import render

def group_dashboard(request):
    return render(request, 'groups/group_dashboard.html')