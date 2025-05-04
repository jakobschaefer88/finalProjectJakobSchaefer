import calendar
from datetime import date
from django.shortcuts import render, redirect
from .widgets import registry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from calendarApp.models import UserWidgetConfig


def generate_month_calendar(year, month):
    cal = calendar.Calendar(firstweekday=6)  # Week starts on Sunday
    month_days = cal.itermonthdays4(year, month)
    weeks = []

    week = []
    for day in month_days:
        y, m, d, weekday = day
        if m == month:
            week.append({
                'day': d,
                'date': date(y, m, d),
                'current_month': True,
            })
        else:
            week.append({
                'day': d,
                'date': date(y, m, d),
                'current_month': False,
            })

        if len(week) == 7:
            weeks.append(week)
            week = []

    return weeks

@login_required
def dashboard(request):
    user = request.user

    today = date.today()
    calendar_weeks = generate_month_calendar(today.year, today.month)

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