from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WidgetInstance
from .widgets import registered_widgets

@login_required
def dashboard(request):
    widget_instances = WidgetInstance.objects.filter(user=request.user).order_by('order')

    widgets = []
    for instance in widget_instances:
        widget_instance = registered_widgets.get(instance.widget_name)
        if widget_instance:
            context = widget_instance.get_context_data(user=request.user, config=instance.config)
            widgets.append({
                "template": widget_instance.template_name,
                "context": context,
            })

    return render(request, "calendarApp/dashboard.html", {"widgets": widgets})

@login_required
def widget_list(request):
    available_widgets = list(registered_widgets.keys())

    if request.method == "POST":
        widget_name = request.POST.get("widget_name")
        if widget_name in registered_widgets:
            WidgetInstance.objects.create(user=request.user, widget_name=widget_name)
            return redirect("calendarApp:dashboard")

        return render(request, "calendarApp/widget_list.html", {"available_widgets": available_widgets})
