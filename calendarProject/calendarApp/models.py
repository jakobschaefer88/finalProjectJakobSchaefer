from django.db import models
from django.contrib.auth.models import User

class GroceryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grocery_items')
    name = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plans')
    date = models.DateField()
    meal = models.TextField()

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date}: {self.meal}"

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_items')
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class TrackedStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracked_stocks')
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.symbol.upper()}"