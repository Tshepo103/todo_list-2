from django import forms
from .models import Task

COLOR_CHOICES = [
    ('', 'No Color'),  # <-- blank choice
    ('#FF0000', 'Red'),
    ('#00FF00', 'Green'),
    ('#0000FF', 'Blue'),
]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'color', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'color_code': forms.TextInput(attrs={'type': 'color'}),
        }