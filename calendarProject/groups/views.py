from django.shortcuts import render
from .models import Group

def group_dashboard(request):
    user_groups = request.user.groups.all()
    return render(request, "groups/group_dashboard.html", {"groups": user_groups})