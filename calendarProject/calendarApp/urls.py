from django.urls import path
from . import views

app_name = 'calendarApp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("widgets/weather/update/", views.update_weather_city, name="update_weather_city"),
]