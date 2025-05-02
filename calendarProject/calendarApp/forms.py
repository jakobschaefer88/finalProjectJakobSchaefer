from django import forms
from .models import GroceryItem, TodoItem, MealPlan, TrackedStock

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['text']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class TrackedStockForm(forms.ModelForm):
    class Meta:
        model = TrackedStock
        fields = ['symbol']