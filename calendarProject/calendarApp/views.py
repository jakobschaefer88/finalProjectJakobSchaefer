import calendar
from datetime import date
from django.shortcuts import render
from .widgets import registry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import GroceryItem
from .forms import GroceryItemForm

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
    user = request.user if request.user.is_authenticated else None

    # Get today's date
    today = date.today()
    calendar_weeks = generate_month_calendar(today.year, today.month)

    # Load all registered widgets
    rendered_widgets = []
    for widget_class in registry:
        widget = widget_class()
        html = widget.render(user=user)
        rendered_widgets.append(html)

    context = {
        "calendar_weeks": calendar_weeks,
        "rendered_widgets": rendered_widgets,
        "month": today.strftime("%B"),
        "year": today.year,
    }

    return render(request, "calendarApp/dashboard.html", context)

@csrf_exempt
def grocery_list_view(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = user
            item.save()
            return JsonResponse({"success": True, "item": item.name})
        return JsonResponse({"success": False, "errors": form.errors})

    elif request.method == "GET":
        items = GroceryItem.objects.filter(user=user).values("id", "name", "completed")
        return JsonResponse(list(items), safe=False)