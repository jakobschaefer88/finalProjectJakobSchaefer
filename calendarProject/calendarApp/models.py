'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Models File

'''

from django.db import models
from django.contrib.auth.models import User

#Links each widget to specific user
class UserWidgetConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    widget_name = models.CharField(max_length=100)
    config = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.widget_name}"

#Used for each user
class TrackedStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracked_stocks')
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.symbol.upper()}"

#used for each user
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} on {self.date}"