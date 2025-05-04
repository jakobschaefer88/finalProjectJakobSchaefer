from django.db import models
from django.contrib.auth.models import User

class UserWidgetConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    widget_name = models.CharField(max_length=100)
    config = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.widget_name}"

class TrackedStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracked_stocks')
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.symbol.upper()}"
