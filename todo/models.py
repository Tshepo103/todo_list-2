from django.db import models
from django.utils import timezone

COLOR_CHOICES = [
    ('', 'No Color'),
    ('#f8d7da', 'Light Red'),
    ('#d1e7dd', 'Light Green'),
    ('#cff4fc', 'Light Blue'),
    ('#fff3cd', 'Light Yellow'),
    ('#e2e3f3', 'Lavender'),
    ('#f0f0f0', 'Light Grey'),
]

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def time_left(self):
        return self.due_date - timezone.now()
