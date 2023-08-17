from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'author': forms.HiddenInput }
