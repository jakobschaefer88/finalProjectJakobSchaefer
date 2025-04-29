import calendar
from datetime import date, datetime, timedelta

def get_month_calendar(year, month, events):
    cal = calendar.Calendar(firstweekday=6)  # Week starts on Sunday
    month_days = cal.itermonthdates(year, month)

    month_calendar = []
    for week in range(6):  # Always 6 weeks for simplicity
        week_days = []
        for day in range(7):
            current_date = next(month_days)
            day_events = [event for event in events if event.start_time.date() == current_date]
            week_days.append({
                "date": current_date,
                "is_current_month": current_date.month == month,
                "events": day_events
            })
        month_calendar.append(week_days)

    return month_calendar