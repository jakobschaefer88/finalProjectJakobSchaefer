from django import forms
from .models import TrackedStock, Event

class TrackedStockForm(forms.ModelForm):
    class Meta:
        model = TrackedStock
        fields = ['symbol']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time']