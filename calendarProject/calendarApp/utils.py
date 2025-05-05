'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Utils File

'''

import calendar

#Creates a calendar with day starting on Sunday
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

    #return the month calendar with event data
    return month_calendar