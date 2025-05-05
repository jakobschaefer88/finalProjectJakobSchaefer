import calendar
from datetime import date
from .widgets import registry
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from calendarApp.models import UserWidgetConfig, Event
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST


def generate_month_calendar(year, month, events=[]):
    cal = calendar.Calendar(firstweekday=6)  # Week starts on Sunday
    month_days = cal.itermonthdays4(year, month)
    weeks = []

    today = timezone.localdate()  # Get today's date for comparison
    week = []
    for day in month_days:
        y, m, d, weekday = day
        day_date = date(y, m, d)
        events_on_day = [event for event in events if event.date == day_date]  # Find events on this date
        if m == month:
            week.append({
                'day': d,
                'date': day_date,
                'current_month': True,
                'is_today': day_date == today,
                'events': events_on_day  # Add events for this day
            })
        else:
            week.append({
                'day': d,
                'date': day_date,
                'current_month': False,
                'is_today': day_date == today,
                'events': events_on_day  # Add events for this day
            })

        if len(week) == 7:
            weeks.append(week)
            week = []

    return weeks


@login_required
def dashboard(request):
    user = request.user

    today = timezone.localdate()

    # Get all events for the current user in the current month
    events = Event.objects.filter(user=user, date__year=today.year, date__month=today.month)

    # Update the calendar with the events
    calendar_weeks = generate_month_calendar(today.year, today.month, events)

    # Render widgets (if you have any)
    rendered_widgets = []
    for widget_class in registry:
        widget = widget_class()
        html = widget.render(user=user, request=request)  # Pass request here
        rendered_widgets.append(html)

    context = {
        "calendar_weeks": calendar_weeks,
        "rendered_widgets": rendered_widgets,
        "month": today.strftime("%B"),
        "year": today.year,
    }

    return render(request, "calendarApp/dashboard.html", context)


@login_required
def update_weather_city(request):
    city = request.POST.get('city', 'London')
    user = request.user

    # Update or create the widget configuration
    UserWidgetConfig.objects.update_or_create(
        user=user, widget_name='weather',
        defaults={'config': {'city': city}}
    )

    return JsonResponse({'status': 'success', 'city': city})


@require_POST
@login_required
def add_event(request):
    event_date = request.POST.get("event_date")
    title = request.POST.get("event_text")
    description = request.POST.get("event_description", "")

    if event_date and title:
        Event.objects.create(
            user=request.user,
            date=event_date,
            title=title,
            description=description
        )
        messages.success(request, "Event added successfully!")
    else:
        messages.error(request, "Please provide both date and event title.")

    return redirect('calendarApp:dashboard')