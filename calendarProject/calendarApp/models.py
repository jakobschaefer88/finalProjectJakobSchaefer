from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    allDay = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WidgetInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    widget_name = models.CharField(max_length=100)
    config = models.JSONField(default=dict)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.widget_name} for {self.user.username}"

