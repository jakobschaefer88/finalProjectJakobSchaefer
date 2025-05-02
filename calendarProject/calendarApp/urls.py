from django.urls import path
from . import views

app_name = 'calendarApp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('widgets/grocery/', views.grocery_list_view, name='grocery_list'),
]