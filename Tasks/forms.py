from django import forms

from Tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline', 'done')
