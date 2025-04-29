from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WidgetInstance, Event
from .widgets import registered_widgets
from .forms import EventForm
from datetime import datetime
from .utils import get_month_calendar
from calendar import monthrange

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

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user).order_by('startTime')
    return render(request, "calendarApp/event_list.html", {"events": events})

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')

        else:
            form = EventForm()
        return render(request, "calendarApp/event_form.html", {"form": form})

@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        else:
            form = EventForm(instance=event)
        return render(request, "calendarApp/event_form.html", {"form": form})

@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('event_list')

@login_required
def calendar_view(request):
    today = datetime.today()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    # Correct month and year overflow
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    events = Event.objects.filter(user=request.user, start_time__year=year, start_time__month=month)
    month_calendar = get_month_calendar(year, month, events)

    # Calculate previous and next month
    prev_month = month - 1
    prev_year = year
    next_month = month + 1
    next_year = year

    if prev_month < 1:
        prev_month = 12
        prev_year -= 1
    if next_month > 12:
        next_month = 1
        next_year += 1

    return render(request, "calendar_app/calendar.html", {
        "month_calendar": month_calendar,
        "year": year,
        "month": month,
        "prev_month": prev_month,
        "prev_year": prev_year,
        "next_month": next_month,
        "next_year": next_year,
    })

@login_required
def widgets(request):
    return render(request, "calendarApp/widget_list.html")