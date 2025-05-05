'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Urls File

'''

from django.urls import path
from . import views

#Defined the app name for namespacing urls
app_name = 'calendarApp'

urlpatterns = [
    #URL for dashboard view
    path('', views.dashboard, name='dashboard'),
    #URL for updating the weather
    path("widgets/weather/update/", views.update_weather_city, name="update_weather_city"),
    #url for adding an event
    path('add-event/', views.add_event, name='add_event'),
]