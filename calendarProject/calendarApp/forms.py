from django import forms
from .models import TrackedStock

class TrackedStockForm(forms.ModelForm):
    class Meta:
        model = TrackedStock
        fields = ['symbol']