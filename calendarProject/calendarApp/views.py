from django.shortcuts import render
from .widgets import registry  # You'll define this in __init__.py of the widgets package

def dashboard(request):
    user = request.user if request.user.is_authenticated else None

    # Load all registered widgets
    rendered_widgets = []
    for widget_class in registry:
        widget = widget_class()
        html = widget.render(user=user)
        rendered_widgets.append(html)

    context = {
        "rendered_widgets": rendered_widgets
    }

    return render(request, "calendarApp/dashboard.html", context)