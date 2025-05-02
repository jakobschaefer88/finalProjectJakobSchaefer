from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('widgets/grocery/', views.grocery_list_view, name='grocery_list'),
]