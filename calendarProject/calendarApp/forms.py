from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'startTime', 'endTime', 'allDay']
        widgets = {
            'startTime': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'endTime': forms.TimeInput(attrs={'type': 'datetime-local'}),
        }