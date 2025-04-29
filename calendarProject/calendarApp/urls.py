from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('widgets/', views.widgets, name='widgets'),
    path('events/', views.event_list, name='events_list'),
    path('events/new/', views.event_create, name='event_create'),
    path('events/<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('calendar/', views.calendar_view, name='calendar_view'),
]